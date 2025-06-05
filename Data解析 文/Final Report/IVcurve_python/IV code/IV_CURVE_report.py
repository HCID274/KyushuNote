# Data解析 文\Final Report\IVcurve_python\IV code\IV_CURVE_report.py
import os
import numpy as np
import matplotlib.pyplot as plt
import daq as dq
import probe_analysis as probe # 假设 probe_analysis.py 在同目录下或Python路径中

# --- 基本设置 ---
# 定义数据存储的基础路径 (Windows路径，使用原始字符串r"..."或正斜杠"/")

# !! 请务必根据你的实际文件夹名称调整格式化字符串 {:02d} 或 {:05d} !!

base_dir = r"D:\Files\HCI\修士\04笔记\Data解析 文\Final Report\IVcurve_python\data/{:02d}"
plt.rcParams['figure.dpi'] = 100 # 设置图像DPI

# --- 常量和参数 ---
npoint = 20000                 # 每个扫描周期（或半周期）的数据点数
file_num_start = 1             # 数据文件夹的起始编号 (例如，01, 02 ...)
num_radial_positions = 9       # 要分析的径向位置数量
k_boltzmann = 1.38e-23         # 玻尔兹曼常数 (J/K)
m_ion_kg = 6.65e-26            # 离子质量 (kg) - 假设是氩气
m_electron_kg = 9.11e-31       # 电子质量 (kg)
q_electron = 1.6e-19           # 元电荷 (C)
s_probe_area_m2 = 6.47625e-6   # 探针收集面积 (m^2)

# 径向位置 (cm)，与数据文件夹对应 (根据幻灯片P5)
radial_positions_cm = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
if len(radial_positions_cm) != num_radial_positions:
    raise ValueError("Number of radial positions does not match the length of the defined list") # 英文UI

# --- 用于存储所有径向位置结果的列表 ---
all_Te_eV = []
all_ne_m3 = []       # 初始存储单位为 m^-3
all_Vs_V = []
all_Vf_V = []        # 浮动电位

# --- 初始化数据采集对象 ---
fid = dq.pantaADC()

# --- 创建用于保存图像的文件夹 ---
output_pic_dir = "pics"
os.makedirs(output_pic_dir, exist_ok=True) # 在循环外创建一次即可

# --- 主循环：处理每个径向位置的数据 ---
for i in range(num_radial_positions):
    current_filen_nr = file_num_start + i
    dir_path = base_dir.format(current_filen_nr)
    current_radial_pos_cm = radial_positions_cm[i]
    print(f"\nProcessing Radial Position {current_radial_pos_cm} cm (Folder: {dir_path})") # 英文UI

    # 初始化当前位置的参数为 NaN，以便在出错时有默认值
    Te_eV_current = np.nan
    ne_m3_current = np.nan
    Vs_V_current = np.nan
    Vf_V_current = np.nan

    try:
        # 读取原始数据文件
        raw_current_A_orig, time_s = fid.read(basename="1_3_09", dir=dir_path, gzipped=False, samplingtime=True)
        sweep_voltage_V_orig, time_s_sweep = fid.read(basename="1_3_11", dir=dir_path, gzipped=False, samplingtime=True)
        # 假设 time_s 和 time_s_sweep 应该相同或兼容
        if not np.array_equal(time_s, time_s_sweep):
            print(f"  Warning: Time axes for current and voltage at radial position {current_radial_pos_cm} cm are not identical. Using current's time axis.") # 英文UI

    except Exception as e:
        print(f"  Error: Failed to read data for radial position {current_radial_pos_cm} cm: {e}") # 英文UI
        all_Te_eV.append(Te_eV_current)
        all_ne_m3.append(ne_m3_current)
        all_Vs_V.append(Vs_V_current)
        all_Vf_V.append(Vf_V_current)
        continue # 跳到下一个径向位置

    # 数据预处理 (校准)
    sweep_voltage_V_cal = sweep_voltage_V_orig * 100  # [V]
    raw_current_A_cal = -1.0 * raw_current_A_orig / 20  # [A]

    # 选择分析的时间范围
    start_index = 200000
    end_index = 500000
    if len(time_s) < end_index: # 检查数据长度是否足够
        print(f"  Warning: Data length ({len(time_s)}) at radial position {current_radial_pos_cm} cm is less than expected end point ({end_index}). Using actual data length.") # 英文UI
        end_index = len(time_s)
    if start_index >= end_index:
        print(f"  Error: Start index ({start_index}) out of range for radial position {current_radial_pos_cm} cm (adjusted end point: {end_index}).") # 英文UI
        all_Te_eV.append(Te_eV_current)
        all_ne_m3.append(ne_m3_current)
        all_Vs_V.append(Vs_V_current)
        all_Vf_V.append(Vf_V_current)
        continue

    time_s_sliced = time_s[start_index:end_index]
    sweep_voltage_V_sliced = sweep_voltage_V_cal[start_index:end_index]
    raw_current_A_sliced = raw_current_A_cal[start_index:end_index]

    if len(time_s_sliced) == 0: # 如果切片后数据为空
        print(f"  Error: Data slice is empty for radial position {current_radial_pos_cm} cm.") # 英文UI
        all_Te_eV.append(Te_eV_current)
        all_ne_m3.append(ne_m3_current)
        all_Vs_V.append(Vs_V_current)
        all_Vf_V.append(Vf_V_current)
        continue

    # 对扫描数据进行排序和平均 (得到平均的I-V特性)
    try:
        # sweep_sort 返回: 平均时间点, 多个扫描周期的电压(2D), 多个扫描周期的电流(2D), 扫描周期数
        time_avg_s_points, sweep_V_cycles, raw_A_cycles, nsweep = probe.sweep_sort(
            time_s_sliced, sweep_voltage_V_sliced, raw_current_A_sliced, npoint
        )
        if nsweep == 0:
            print(f"  Warning: nsweep is 0 after sweep_sort for radial position {current_radial_pos_cm} cm.") # 英文UI
            raise ValueError("nsweep is 0")

        # 取所有扫描周期的平均值得到最终用于分析的I-V曲线
        sweep_V_final = np.mean(sweep_V_cycles, axis=0)
        raw_A_final = np.mean(raw_A_cycles, axis=0)

    except Exception as e:
        print(f"  Error: Error during sweep_sort or averaging for radial position {current_radial_pos_cm} cm: {e}") # 英文UI
        all_Te_eV.append(Te_eV_current)
        all_ne_m3.append(ne_m3_current)
        all_Vs_V.append(Vs_V_current)
        all_Vf_V.append(Vf_V_current)
        continue

    # --- 参数提取 ---
    try:
        # 1. 计算浮动电位 (Vf)
        Vf_V_current = probe.floating(sweep_V_final, raw_A_final)
        # print(f"  Vf = {Vf_V_current:.2f} V") # probe.floating 内部已经打印 (presumably in English or needs check in probe_analysis.py)

        # 2. 拟合离子电流并计算电子电流
        # !! 离子电流拟合范围 (vmin, vmax) 可能也需要根据Vf调整，或更智能地确定 !!
        #    暂时使用原始值，但要注意这可能影响电子电流的准确性
        ion_fit_vmin = -45
        ion_fit_vmax = -20 # Vf - 20 (Vf - 20*Te)
        # 如果 Vf 很低 (例如接近0或负值)，上述固定范围可能不合适
        # 一个更安全的做法是确保离子电流拟合范围远低于 Vf
        if Vf_V_current < ion_fit_vmax + 5: # 如果 Vf 比较高，使得 -20V 离 Vf 太近或超过
            ion_fit_vmax = Vf_V_current - 20 # 尝试从 Vf 向下20V
            if ion_fit_vmax < ion_fit_vmin + 5: # 确保 vmax 仍然大于 vmin 且有足够范围
                ion_fit_vmax = ion_fit_vmin + 5 # 最小范围
                print(f"  Warning: Adjusted ion current fit upper limit {ion_fit_vmax:.2f}V is low.") # 英文UI

        ion_current_A_fit = probe.fit_ion_current(sweep_V_final, raw_A_final, vmin=ion_fit_vmin, vmax=ion_fit_vmax)
        electron_current_A = raw_A_final - ion_current_A_fit

        # 3. 计算电子密度 (ne)，暂时使用原始脚本中的基于离子饱和电流的方法
        # !! 这个公式和其中的 '2000' 因子需要仔细验证其来源和适用性 !!
        # !! 用于取离子饱和电流的索引范围 [500:2000] 是经验性的，可能不适用于所有情况 !!
        #    理想情况下，应从拟合的 ion_current_A_fit 中安全地提取饱和值
        idx_ion_sat_start = np.argmin(np.abs(sweep_V_final - (ion_fit_vmin + 1))) # 尝试在拟合区域内取点
        idx_ion_sat_end = np.argmin(np.abs(sweep_V_final - (ion_fit_vmax -1 )))
        if idx_ion_sat_start >= idx_ion_sat_end : # 如果范围太小或无效
             selected_ion_current = ion_current_A_fit[0:int(len(ion_current_A_fit)/4)] # 取离子区前1/4做平均
        else:
            selected_ion_current = ion_current_A_fit[idx_ion_sat_start : idx_ion_sat_end]

        if len(selected_ion_current) > 0:
            ion_sat_current_A_estimate = np.mean(selected_ion_current[selected_ion_current < 0]) # 只取负值部分平均
            if not np.isnan(ion_sat_current_A_estimate):
                 ne_m3_current = (np.exp(0.5) * np.abs(ion_sat_current_A_estimate)) / \
                                 ((q_electron * s_probe_area_m2) * 2000) # 那个2000!
                 print(f"  ne (from ion sat.) = {ne_m3_current:.2e} m^-3") # 英文UI
            else:
                print(f"  Warning: Cannot estimate valid ion saturation current from ion current.") # 英文UI
                ne_m3_current = np.nan
        else:
            print(f"  Warning: Selected ion current data for estimating ion saturation current is empty.") # 英文UI
            ne_m3_current = np.nan


        # 4. 计算电子温度 (Te)
        if np.isnan(Vf_V_current):
            print(f"  Skipping Te calculation because Vf is NaN.") # 英文UI
            Te_eV_current = np.nan
        else:
            # 动态设定Te拟合范围：从 Vf 以上一点开始，跨越一定电压范围
            te_fit_vf_offset = 0.5  # Te拟合起始点高于Vf的电压 (V)
            te_fit_span = 5.0      # Te拟合窗口的电压跨度 (V)
                                   # 这个跨度理想情况下应为几倍的Te，但Te未知，所以先用固定值
                                   # 对于高温等离子体，这个span可能需要更大

            te_vmin_actual = Vf_V_current + te_fit_vf_offset
            te_vmax_actual = te_vmin_actual + te_fit_span
            print(f"  Te fit range: Vmin={te_vmin_actual:.2f} V, Vmax={te_vmax_actual:.2f} V") # 英文UI

            # 在调用 fit_te 前，筛选出该电压范围内的电子电流，并确保其为正
            # probe_analysis.py 中的 fit_te 接收 sweep 和 ie，内部再根据 vmin, vmax 筛选
            # 我们需要确保传递给它的 ie 在这个 vmin, vmax 范围内大部分是正的
            # （理想的修改是在 probe_analysis.py 的 fit_te 内部做更严格的检查）
            
            # 筛选出用于拟合Te的电压和电子电流部分
            mask_te_fit_range = (sweep_V_final >= te_vmin_actual) & (sweep_V_final <= te_vmax_actual)
            ie_for_te_fit_check = electron_current_A[mask_te_fit_range]

            if len(ie_for_te_fit_check[ie_for_te_fit_check > 0]) < 2: # 如果正电流点少于2个
                print(f"  Warning: Not enough positive electron current data points in the selected Te fit range ({te_vmin_actual:.2f}-{te_vmax_actual:.2f}V).") # 英文UI
                Te_eV_current = np.nan
            else:
                try:
                    Te_eV_current, Te_b_fit_param = probe.fit_te(sweep_V_final, electron_current_A,
                                                                 vmin=te_vmin_actual, vmax=te_vmax_actual)
                    # print(f"  Te = {Te_eV_current:.2f} eV") # probe.fit_te 内部已打印
                    if np.isnan(Te_eV_current) or Te_eV_current <= 0.05 or Te_eV_current > 50: # 检查Te的合理性
                        print(f"  Warning: Calculated Te ({Te_eV_current:.2f} eV) is unreasonable, set to NaN.") # 英文UI
                        Te_eV_current = np.nan
                except Exception as te_err:
                    print(f"  Error: Error during Te calculation: {te_err}") # 英文UI
                    Te_eV_current = np.nan

        # 5. 计算空间电位 (Vs)
        if np.isnan(Te_eV_current) or np.isnan(Vf_V_current):
            print(f"  Skipping Vs calculation because Te or Vf is NaN.") # 英文UI
            Vs_V_current = np.nan
        else:
            # Vs 的拟合范围也应动态调整，通常在 Te 拟合结束点之上，电子电流开始饱和的区域
            # 这里使用一个简化的策略：从Te拟合结束点再往上几倍Te的位置开始
            vs_fit_te_offset_factor = 2 # Vs拟合起始点高于(Vf + Te_span)约几倍Te (估算)
            vs_fit_vmin_actual = te_vmax_actual + vs_fit_te_offset_factor * max(1, Te_eV_current) # 用max(1,Te)避免Te太小时偏移过小
            vs_fit_span = 10.0 # Vs拟合窗口的电压跨度 (V) - 这个也需要调整
            vs_fit_vmax_actual = vs_fit_vmin_actual + vs_fit_span
            # 确保不超过最大扫描电压
            if len(sweep_V_final)>0 :
                vs_fit_vmax_actual = min(vs_fit_vmax_actual, np.max(sweep_V_final) - 0.5)
            
            if vs_fit_vmin_actual >= vs_fit_vmax_actual -1 : # 如果拟合范围不合理
                 print(f"  Warning: Vs fit range is unreasonable (Vmin={vs_fit_vmin_actual:.2f}, Vmax={vs_fit_vmax_actual:.2f}). Trying fixed upper limit.") # 英文UI
                 # 尝试一个固定但可能较高的上限，依赖fit_vs内部逻辑
                 vs_fit_vmax_actual = np.max(sweep_V_final) - 0.5 if len(sweep_V_final)>0 else vs_fit_vmin_actual + 5


            print(f"  Vs fit range: Vmin={vs_fit_vmin_actual:.2f} V, Vmax={vs_fit_vmax_actual:.2f} V") # 英文UI
            try:
                Vs_V_current, _, _ = probe.fit_vs(sweep_V_final, electron_current_A, Te_eV_current, Te_b_fit_param,
                                                  vmin=vs_fit_vmin_actual, vmax=vs_fit_vmax_actual)
                # print(f"  Vs = {Vs_V_current:.2f} V") # probe.fit_vs 内部已打印
            except Exception as vs_err:
                print(f"  Error: Error during Vs calculation: {vs_err}") # 英文UI
                Vs_V_current = np.nan

    except Exception as analysis_error:
        print(f"  Critical Error: Uncaught error during analysis for radial position {current_radial_pos_cm} cm: {analysis_error}") # 英文UI
        # 确保即使在此处出错，也填充NaN
        Te_eV_current = np.nan
        ne_m3_current = np.nan
        Vs_V_current = np.nan
        Vf_V_current = Vf_V_current if 'Vf_V_current' in locals() and not np.isnan(Vf_V_current) else np.nan


    # 将当前位置的计算结果（或NaN）存入总列表
    all_Te_eV.append(Te_eV_current)
    all_ne_m3.append(ne_m3_current)
    all_Vs_V.append(Vs_V_current)
    all_Vf_V.append(Vf_V_current)

    # --- 可选：为每个位置绘制调试图 ---
    # if True: # 设置为True以显示每个位置的图，或根据条件(例如 if np.isnan(Te_eV_current))显示
    #     plt.figure(figsize=(12, 5))
    #     plt.suptitle(f"Debug Plot: Radial Position {current_radial_pos_cm} cm", fontsize=14) # 英文UI

    #     # 子图1: I-V 曲线和离子电流拟合
    #     plt.subplot(1, 2, 1)
    #     plt.plot(sweep_V_final, raw_A_final * 1000, "k-", label="Raw $I_p$ (averaged)", markersize=2) # 英文UI
    #     if 'ion_current_A_fit' in locals():
    #         plt.plot(sweep_V_final, ion_current_A_fit * 1000, "r--", label="Ion Current $I_i$ (fitted)") # 英文UI
    #     if 'electron_current_A' in locals():
    #          plt.plot(sweep_V_final, electron_current_A * 1000, "b:", label="Electron Current $I_e$ ($I_p - I_i$)") # 英文UI
    #     plt.axhline(0, color='gray', lw=0.5)
    #     plt.axvline(Vf_V_current if not np.isnan(Vf_V_current) else 0, color='purple', linestyle='--', label=f"Vf={Vf_V_current:.2f}V" if not np.isnan(Vf_V_current) else "Vf=NaN") # 英文UI
    #     plt.xlabel("$V_{probe}$ (V)")
    #     plt.ylabel("$I_{probe}$ (mA)")
    #     plt.title("I-V Curve") # 英文UI
    #     plt.grid(True, linestyle=':')
    #     plt.legend()

    #     # 子图2: 半对数电子电流和拟合参数
    #     plt.subplot(1, 2, 2)
    #     if 'electron_current_A' in locals():
    #         # 只绘制电子电流为正的部分，避免log警告
    #         valid_ie_mask = electron_current_A > 1e-7 # 用一个很小的正数作为阈值
    #         if np.any(valid_ie_mask):
    #             plt.plot(sweep_V_final[valid_ie_mask], electron_current_A[valid_ie_mask] * 1000, "b-", label="$I_e > 0$")
    #         else:
    #             plt.text(0.5, 0.5, "No valid positive electron current data", ha='center', va='center', transform=plt.gca().transAxes) # 英文UI

    #         # 标注Te拟合区域
    #         if 'te_vmin_actual' in locals() and 'te_vmax_actual' in locals():
    #             plt.axvspan(te_vmin_actual, te_vmax_actual, color='green', alpha=0.2, label=f"Te Fit Region\n({Te_eV_current:.2f}eV)" if not np.isnan(Te_eV_current) else "Te Fit Region (Failed)") # 英文UI
    #         # 标注Vs拟合区域 (如果适用)
    #         if 'vs_fit_vmin_actual' in locals() and 'vs_fit_vmax_actual' in locals():
    #              plt.axvspan(vs_fit_vmin_actual, vs_fit_vmax_actual, color='orange', alpha=0.2, label=f"Vs Fit Region\n({Vs_V_current:.2f}V)" if not np.isnan(Vs_V_current) else "Vs Fit Region (Failed)") # 英文UI
        
    #     plt.axvline(Vf_V_current if not np.isnan(Vf_V_current) else 0, color='purple', linestyle='--', label="Vf")
    #     plt.axvline(Vs_V_current if not np.isnan(Vs_V_current) else 0, color='red', linestyle='-.', label="Vs")

    #     plt.yscale("log")
    #     min_current_plot = np.min(electron_current_A[electron_current_A > 1e-7] * 1000) if np.any(electron_current_A > 1e-7) else 1e-2
    #     max_current_plot = np.max(electron_current_A[electron_current_A > 1e-7] * 1000) if np.any(electron_current_A > 1e-7) else 1e3
    #     if min_current_plot >= max_current_plot : min_current_plot=1e-2; max_current_plot=1e3 # 确保范围有效
    #     plt.ylim(min_current_plot * 0.5 , max_current_plot * 2)


    #     plt.xlabel("$V_{probe}$ (V)")
    #     plt.ylabel("$I_e$ (mA) - log scale")
    #     plt.title("Electron Current (log scale)") # 英文UI
    #     plt.grid(True, which="both", linestyle=':')
    #     plt.legend(fontsize='small')
        
    #     plt.tight_layout(rect=[0, 0, 1, 0.96]) # 为总标题留空间
    #     plt.show()


# --- 最终结果绘图：径向分布 ---

# 电子密度单位转换: 从 m^-3 转换为 (x 10^9 cm^-3)
# 1 m^-3 = 1e-6 cm^-3.  (ne_m3 * 1e-6) / 1e9 = ne_m3 * 1e-15
all_ne_plot_units = [(val * 1e-15) if not np.isnan(val) else np.nan for val in all_ne_m3]

plt.figure(figsize=(7, 5))
plt.plot(radial_positions_cm, all_Te_eV, marker='o', linestyle='-', color='red', label='$T_e$')
plt.xlabel("Radial Position r (cm)", fontsize=12) 
plt.ylabel("$T_e$ (eV)", fontsize=12)
plt.title("Electron Temperature Radial Profile", fontsize=14) 
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_pic_dir, f"Te_radial_profile.png")) # 保存图像
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(radial_positions_cm, all_ne_plot_units, marker='s', linestyle='-', color='blue', label='$n_e$')
plt.xlabel("Radial Position r (cm)", fontsize=12) 
plt.ylabel("$n_e$ (x $10^9$ cm$^{-3}$)", fontsize=12) 
plt.title("Electron Density Radial Profile", fontsize=14) 
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_pic_dir, f"ne_radial_profile.png")) # 保存图像
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(radial_positions_cm, all_Vs_V, marker='^', linestyle='-', color='green', label='$\phi_s$')
plt.xlabel("Radial Position r (cm)", fontsize=12) 
plt.ylabel("$\phi_s$ (V)", fontsize=12)
plt.title("Space Potential Radial Profile", fontsize=14) 
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_pic_dir, f"Vs_radial_profile.png")) # 保存图像
plt.show()

# --- 打印最终数值结果 ---
print("\n--- Analysis Complete ---") # 英文UI
print(f"Radial Positions (cm): {radial_positions_cm}") # 英文UI
print(f"Floating Potential Vf (V): {[f'{v:.2f}' if not np.isnan(v) else 'NaN' for v in all_Vf_V]}") # 英文UI
print(f"Electron Temperature Te (eV): {[f'{t:.2f}' if not np.isnan(t) else 'NaN' for t in all_Te_eV]}") # 英文UI
print(f"Electron Density ne (m^-3): {[f'{n:.2e}' if not np.isnan(n) else 'NaN' for n in all_ne_m3]}") # 英文UI
print(f"Electron Density ne (x 10^9 cm^-3): {[f'{n:.2f}' if not np.isnan(n) else 'NaN' for n in all_ne_plot_units]}") # 英文UI
print(f"Space Potential Vs (V): {[f'{s:.2f}' if not np.isnan(s) else 'NaN' for s in all_Vs_V]}") # 英文UI