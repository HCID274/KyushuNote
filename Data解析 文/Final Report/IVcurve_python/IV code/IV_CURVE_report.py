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

# --- 用于存储所有径向位置结果的列表 (均值和标准差) ---
all_Te_eV_mean = []
all_ne_m3_mean = []
all_Vs_V_mean = []
all_Vf_V_mean = [] # 浮动电位的均值

all_Te_eV_std = []
all_ne_m3_std = []
all_Vs_V_std = []
# all_Vf_V_std = [] # 如果需要Vf的标准差

# --- 初始化数据采集对象 ---
fid = dq.pantaADC()

# --- 创建用于保存图像的文件夹 ---
output_pic_dir = "pics"
os.makedirs(output_pic_dir, exist_ok=True)

# --- 主循环：处理每个径向位置的数据 ---
for i in range(num_radial_positions):
    current_filen_nr = file_num_start + i
    dir_path = base_dir.format(current_filen_nr)
    current_radial_pos_cm = radial_positions_cm[i]
    print(f"\nProcessing Radial Position {current_radial_pos_cm} cm (Folder: {dir_path})")

    # 初始化当前位置的参数列表 (用于存储每个周期的结果)
    current_pos_Te_eV_list = []
    current_pos_ne_m3_list = []
    current_pos_Vs_V_list = []
    current_pos_Vf_V_list = []

    # 初始化最终添加到 all_..._mean/std 列表的值为 NaN
    Te_eV_current_mean = np.nan
    ne_m3_current_mean = np.nan
    Vs_V_current_mean = np.nan
    Vf_V_current_mean = np.nan
    Te_eV_current_std = np.nan
    ne_m3_current_std = np.nan
    Vs_V_current_std = np.nan

    try:
        raw_current_A_orig, time_s = fid.read(basename="1_3_09", dir=dir_path, gzipped=False, samplingtime=True)
        sweep_voltage_V_orig, time_s_sweep = fid.read(basename="1_3_11", dir=dir_path, gzipped=False, samplingtime=True)
        if not np.array_equal(time_s, time_s_sweep):
            print(f"  Warning: Time axes for current and voltage at radial position {current_radial_pos_cm} cm are not identical. Using current's time axis.")

    except Exception as e:
        print(f"  Error: Failed to read data for radial position {current_radial_pos_cm} cm: {e}")
        all_Te_eV_mean.append(Te_eV_current_mean)
        all_ne_m3_mean.append(ne_m3_current_mean)
        all_Vs_V_mean.append(Vs_V_current_mean)
        all_Vf_V_mean.append(Vf_V_current_mean)
        all_Te_eV_std.append(Te_eV_current_std)
        all_ne_m3_std.append(ne_m3_current_std)
        all_Vs_V_std.append(Vs_V_current_std)
        continue

    sweep_voltage_V_cal = sweep_voltage_V_orig * 100
    raw_current_A_cal = -1.0 * raw_current_A_orig / 20

    start_index = 200000
    end_index = 500000
    if len(time_s) < end_index:
        print(f"  Warning: Data length ({len(time_s)}) at radial position {current_radial_pos_cm} cm is less than expected end point ({end_index}). Using actual data length.")
        end_index = len(time_s)
    if start_index >= end_index:
        print(f"  Error: Start index ({start_index}) out of range for radial position {current_radial_pos_cm} cm (adjusted end point: {end_index}).")
        all_Te_eV_mean.append(Te_eV_current_mean) # Append NaN
        # ... (append NaNs for all mean and std lists)
        all_ne_m3_mean.append(ne_m3_current_mean)
        all_Vs_V_mean.append(Vs_V_current_mean)
        all_Vf_V_mean.append(Vf_V_current_mean)
        all_Te_eV_std.append(Te_eV_current_std)
        all_ne_m3_std.append(ne_m3_current_std)
        all_Vs_V_std.append(Vs_V_current_std)
        continue

    time_s_sliced = time_s[start_index:end_index]
    sweep_voltage_V_sliced = sweep_voltage_V_cal[start_index:end_index]
    raw_current_A_sliced = raw_current_A_cal[start_index:end_index]

    if len(time_s_sliced) == 0:
        print(f"  Error: Data slice is empty for radial position {current_radial_pos_cm} cm.")
        all_Te_eV_mean.append(Te_eV_current_mean) # Append NaN
        # ... (append NaNs for all mean and std lists)
        all_ne_m3_mean.append(ne_m3_current_mean)
        all_Vs_V_mean.append(Vs_V_current_mean)
        all_Vf_V_mean.append(Vf_V_current_mean)
        all_Te_eV_std.append(Te_eV_current_std)
        all_ne_m3_std.append(ne_m3_current_std)
        all_Vs_V_std.append(Vs_V_current_std)
        continue

    try:
        time_avg_s_points, sweep_V_cycles, raw_A_cycles, nsweep = probe.sweep_sort(
            time_s_sliced, sweep_voltage_V_sliced, raw_current_A_sliced, npoint
        )
        if nsweep == 0:
            print(f"  Warning: nsweep is 0 after sweep_sort for radial position {current_radial_pos_cm} cm.")
            raise ValueError("nsweep is 0")

        print(f"  Processing {nsweep} sweep cycles for this position.")

        # --- 循环处理每个扫描周期 ---
        for k_sweep in range(nsweep):
            # print(f"    Analyzing cycle {k_sweep + 1}/{nsweep}...") # 可以取消注释以进行详细调试
            sweep_V_single_cycle = sweep_V_cycles[k_sweep, :]
            raw_A_single_cycle = raw_A_cycles[k_sweep, :]

            Vf_V_cycle = np.nan
            ne_m3_cycle = np.nan
            Te_eV_cycle = np.nan
            Vs_V_cycle = np.nan
            Te_b_fit_param_cycle = np.nan # 用于Vs计算

            try:
                # 1. 计算浮动电位 (Vf)
                # 假设 probe.floating 等函数可以接受 verbose 参数来减少输出
                Vf_V_cycle = probe.floating(sweep_V_single_cycle, raw_A_single_cycle, verbose=False if hasattr(probe, 'floating') and 'verbose' in probe.floating.__code__.co_varnames else True)

                # 2. 拟合离子电流并计算电子电流
                ion_fit_vmin_cycle = -45
                ion_fit_vmax_cycle = -20
                if not np.isnan(Vf_V_cycle) and Vf_V_cycle < ion_fit_vmax_cycle + 5:
                    ion_fit_vmax_cycle = Vf_V_cycle - 20
                    if ion_fit_vmax_cycle < ion_fit_vmin_cycle + 5:
                        ion_fit_vmax_cycle = ion_fit_vmin_cycle + 5
                
                ion_current_A_fit_cycle = probe.fit_ion_current(sweep_V_single_cycle, raw_A_single_cycle, vmin=ion_fit_vmin_cycle, vmax=ion_fit_vmax_cycle, verbose=False if hasattr(probe, 'fit_ion_current') and 'verbose' in probe.fit_ion_current.__code__.co_varnames else True)
                electron_current_A_cycle = raw_A_single_cycle - ion_current_A_fit_cycle

                # 3. 计算电子密度 (ne)
                idx_ion_sat_start_cycle = np.argmin(np.abs(sweep_V_single_cycle - (ion_fit_vmin_cycle + 1)))
                idx_ion_sat_end_cycle = np.argmin(np.abs(sweep_V_single_cycle - (ion_fit_vmax_cycle - 1)))
                if idx_ion_sat_start_cycle >= idx_ion_sat_end_cycle :
                    selected_ion_current_cycle = ion_current_A_fit_cycle[0:int(len(ion_current_A_fit_cycle)/4)]
                else:
                    selected_ion_current_cycle = ion_current_A_fit_cycle[idx_ion_sat_start_cycle : idx_ion_sat_end_cycle]

                if len(selected_ion_current_cycle) > 0:
                    ion_sat_current_A_estimate_cycle = np.mean(selected_ion_current_cycle[selected_ion_current_cycle < 0])
                    if not np.isnan(ion_sat_current_A_estimate_cycle) and ion_sat_current_A_estimate_cycle != 0 : # 避免除零
                         ne_m3_cycle = (np.exp(0.5) * np.abs(ion_sat_current_A_estimate_cycle)) / \
                                         ((q_electron * s_probe_area_m2) * 2000) # 仍然使用2000

                # 4. 计算电子温度 (Te)
                if not np.isnan(Vf_V_cycle):
                    te_fit_vf_offset_cycle = 0.5
                    te_fit_span_cycle = 5.0
                    te_vmin_actual_cycle = Vf_V_cycle + te_fit_vf_offset_cycle
                    te_vmax_actual_cycle = te_vmin_actual_cycle + te_fit_span_cycle
                    
                    mask_te_fit_range_cycle = (sweep_V_single_cycle >= te_vmin_actual_cycle) & (sweep_V_single_cycle <= te_vmax_actual_cycle)
                    ie_for_te_fit_check_cycle = electron_current_A_cycle[mask_te_fit_range_cycle]

                    if len(ie_for_te_fit_check_cycle[ie_for_te_fit_check_cycle > 0]) >= 2:
                        Te_eV_cycle, Te_b_fit_param_cycle = probe.fit_te(sweep_V_single_cycle, electron_current_A_cycle,
                                                                         vmin=te_vmin_actual_cycle, vmax=te_vmax_actual_cycle, verbose=False if hasattr(probe, 'fit_te') and 'verbose' in probe.fit_te.__code__.co_varnames else True)
                        if np.isnan(Te_eV_cycle) or Te_eV_cycle <= 0.05 or Te_eV_cycle > 50:
                            Te_eV_cycle = np.nan
                            Te_b_fit_param_cycle = np.nan # 重置如果Te无效
                
                # 5. 计算空间电位 (Vs)
                if not (np.isnan(Te_eV_cycle) or np.isnan(Vf_V_cycle) or np.isnan(Te_b_fit_param_cycle)):
                    vs_fit_te_offset_factor_cycle = 2
                    vs_fit_vmin_actual_cycle = te_vmax_actual_cycle + vs_fit_te_offset_factor_cycle * max(1, Te_eV_cycle)
                    vs_fit_span_cycle = 10.0
                    vs_fit_vmax_actual_cycle = vs_fit_vmin_actual_cycle + vs_fit_span_cycle
                    if len(sweep_V_single_cycle) > 0:
                        vs_fit_vmax_actual_cycle = min(vs_fit_vmax_actual_cycle, np.max(sweep_V_single_cycle) - 0.5)
                    
                    if vs_fit_vmin_actual_cycle < vs_fit_vmax_actual_cycle -1 :
                        Vs_V_cycle, _, _ = probe.fit_vs(sweep_V_single_cycle, electron_current_A_cycle, Te_eV_cycle, Te_b_fit_param_cycle,
                                                          vmin=vs_fit_vmin_actual_cycle, vmax=vs_fit_vmax_actual_cycle, verbose=False if hasattr(probe, 'fit_vs') and 'verbose' in probe.fit_vs.__code__.co_varnames else True)
            except Exception as cycle_err:
                print(f"      Error in cycle {k_sweep+1} analysis: {cycle_err}") # 可以取消注释以进行详细调试
                # 确保即使单个周期分析失败，也添加 NaN 值
                Vf_V_cycle, ne_m3_cycle, Te_eV_cycle, Vs_V_cycle = np.nan, np.nan, np.nan, np.nan
            
            current_pos_Vf_V_list.append(Vf_V_cycle)
            current_pos_ne_m3_list.append(ne_m3_cycle)
            current_pos_Te_eV_list.append(Te_eV_cycle)
            current_pos_Vs_V_list.append(Vs_V_cycle)
        
        # --- 计算当前径向位置参数的均值和标准差 ---
        if len(current_pos_Te_eV_list) > 0: # 确保列表不为空
            Vf_V_current_mean = np.nanmean(current_pos_Vf_V_list)
            ne_m3_current_mean = np.nanmean(current_pos_ne_m3_list)
            Te_eV_current_mean = np.nanmean(current_pos_Te_eV_list)
            Vs_V_current_mean = np.nanmean(current_pos_Vs_V_list)

            # 只有当至少有两个有效数据点时，标准差才有意义
            ne_m3_current_std = np.nanstd(current_pos_ne_m3_list, ddof=1) if np.sum(~np.isnan(current_pos_ne_m3_list)) > 1 else np.nan
            Te_eV_current_std = np.nanstd(current_pos_Te_eV_list, ddof=1) if np.sum(~np.isnan(current_pos_Te_eV_list)) > 1 else np.nan
            Vs_V_current_std = np.nanstd(current_pos_Vs_V_list, ddof=1) if np.sum(~np.isnan(current_pos_Vs_V_list)) > 1 else np.nan
            
            print(f"  Mean Vf = {Vf_V_current_mean:.2f} V")
            print(f"  Mean ne = {ne_m3_current_mean:.2e} m^-3, Std ne = {ne_m3_current_std:.2e} m^-3 (from {np.sum(~np.isnan(current_pos_ne_m3_list))} valid cycles)")
            print(f"  Mean Te = {Te_eV_current_mean:.2f} eV, Std Te = {Te_eV_current_std:.2f} eV (from {np.sum(~np.isnan(current_pos_Te_eV_list))} valid cycles)")
            print(f"  Mean Vs = {Vs_V_current_mean:.2f} V, Std Vs = {Vs_V_current_std:.2f} V (from {np.sum(~np.isnan(current_pos_Vs_V_list))} valid cycles)")

    except Exception as outer_analysis_error:
        print(f"  Critical Error during analysis for radial position {current_radial_pos_cm} cm: {outer_analysis_error}")
        # 确保即使在此处出错，也填充NaN (已在循环开始处初始化为NaN)
    
    # 将当前位置的均值和标准差（或NaN）存入总列表
    all_Vf_V_mean.append(Vf_V_current_mean)
    all_ne_m3_mean.append(ne_m3_current_mean)
    all_Te_eV_mean.append(Te_eV_current_mean)
    all_Vs_V_mean.append(Vs_V_current_mean)

    all_ne_m3_std.append(ne_m3_current_std)
    all_Te_eV_std.append(Te_eV_current_std)
    all_Vs_V_std.append(Vs_V_current_std)

    # --- 可选的每个位置的调试图（基于平均的I-V曲线，如之前） ---
    # 如果需要调试每个周期的拟合，则需要更复杂的绘图逻辑
    # ... (之前的调试绘图代码，如果需要，应使用平均后的 sweep_V_final, raw_A_final)


# --- 注释掉之前的绘图代码 ---
# # 电子密度单位转换: 从 m^-3 转换为 (x 10^9 cm^-3)
# # 1 m^-3 = 1e-6 cm^-3.  (ne_m3 * 1e-6) / 1e9 = ne_m3 * 1e-15
# all_ne_plot_units_old = [(val * 1e-15) if not np.isnan(val) else np.nan for val in all_ne_m3_mean] # 使用均值

# plt.figure(figsize=(7, 5))
# plt.plot(radial_positions_cm, all_Te_eV_mean, marker='o', linestyle='-', color='red', label='$T_e$') # 使用均值
# plt.xlabel("Radial Position r (cm)", fontsize=12) 
# plt.ylabel("$T_e$ (eV)", fontsize=12)
# plt.title("Electron Temperature Radial Profile", fontsize=14) 
# plt.grid(True, linestyle='--')
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(output_pic_dir, f"Te_radial_profile.png")) # 保存图像
# plt.close() # 关闭图像以释放内存

# plt.figure(figsize=(7, 5))
# plt.plot(radial_positions_cm, all_ne_plot_units_old, marker='s', linestyle='-', color='blue', label='$n_e$') # 使用均值
# plt.xlabel("Radial Position r (cm)", fontsize=12) 
# plt.ylabel("$n_e$ (x $10^9$ cm$^{-3}$)", fontsize=12) 
# plt.title("Electron Density Radial Profile", fontsize=14) 
# plt.grid(True, linestyle='--')
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(output_pic_dir, f"ne_radial_profile.png")) # 保存图像
# plt.close() # 关闭图像

# plt.figure(figsize=(7, 5))
# plt.plot(radial_positions_cm, all_Vs_V_mean, marker='^', linestyle='-', color='green', label='$\phi_s$') # 使用均值
# plt.xlabel("Radial Position r (cm)", fontsize=12) 
# plt.ylabel("$\phi_s$ (V)", fontsize=12)
# plt.title("Space Potential Radial Profile", fontsize=14) 
# plt.grid(True, linestyle='--')
# plt.legend()
# plt.tight_layout()
# plt.savefig(os.path.join(output_pic_dir, f"Vs_radial_profile.png")) # 保存图像
# plt.close() # 关闭图像


# --- 新的绘图代码：带误差棒的径向分布 ---

# 电子密度单位转换 (均值和标准差)
all_ne_plot_units_mean = [(val * 1e-15) if not np.isnan(val) else np.nan for val in all_ne_m3_mean]
all_ne_plot_units_std = [(val * 1e-15) if not np.isnan(val) else np.nan for val in all_ne_m3_std]


plt.figure(figsize=(8, 6)) # 稍微大一点的图以便容纳误差棒
plt.errorbar(radial_positions_cm, all_Te_eV_mean, yerr=all_Te_eV_std,
             marker='o', linestyle='-', color='red', label='$T_e$', capsize=5, ecolor='darkred')
plt.xlabel("Radial Position r (cm)", fontsize=12) 
plt.ylabel("$T_e$ (eV)", fontsize=12)
plt.title("Electron Temperature Radial Profile (with Error Bars)", fontsize=14) 
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_pic_dir, "Te_radial_profile_errors.png"))
plt.show()
plt.close()

plt.figure(figsize=(8, 6))
plt.errorbar(radial_positions_cm, all_ne_plot_units_mean, yerr=all_ne_plot_units_std,
             marker='s', linestyle='-', color='blue', label='$n_e$', capsize=5, ecolor='darkblue')
plt.xlabel("Radial Position r (cm)", fontsize=12) 
plt.ylabel("$n_e$ (x $10^9$ cm$^{-3}$)", fontsize=12) 
plt.title("Electron Density Radial Profile (with Error Bars)", fontsize=14) 
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_pic_dir, "ne_radial_profile_errors.png"))
plt.show()
plt.close()

plt.figure(figsize=(8, 6))
plt.errorbar(radial_positions_cm, all_Vs_V_mean, yerr=all_Vs_V_std,
             marker='^', linestyle='-', color='green', label='$\phi_s$', capsize=5, ecolor='darkgreen')
plt.xlabel("Radial Position r (cm)", fontsize=12) 
plt.ylabel("$\phi_s$ (V)", fontsize=12)
plt.title("Space Potential Radial Profile (with Error Bars)", fontsize=14) 
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_pic_dir, "Vs_radial_profile_errors.png"))
plt.show()
plt.close()

# --- 打印最终数值结果 (均值) ---
print("\n--- Analysis Complete (with Error Bar Calculation) ---")
print(f"Radial Positions (cm): {radial_positions_cm}")
print(f"Mean Floating Potential Vf (V): {[f'{v:.2f}' if not np.isnan(v) else 'NaN' for v in all_Vf_V_mean]}")
print(f"Mean Electron Temperature Te (eV): {[f'{t:.2f}' if not np.isnan(t) else 'NaN' for t in all_Te_eV_mean]}")
print(f"Std Dev Electron Temperature Te (eV): {[f'{t:.2f}' if not np.isnan(t) else 'NaN' for t in all_Te_eV_std]}")
print(f"Mean Electron Density ne (m^-3): {[f'{n:.2e}' if not np.isnan(n) else 'NaN' for n in all_ne_m3_mean]}")
print(f"Std Dev Electron Density ne (m^-3): {[f'{n:.2e}' if not np.isnan(n) else 'NaN' for n in all_ne_m3_std]}")
print(f"Mean Electron Density ne (x 10^9 cm^-3): {[f'{n:.2f}' if not np.isnan(n) else 'NaN' for n in all_ne_plot_units_mean]}")
print(f"Std Dev Electron Density ne (x 10^9 cm^-3): {[f'{n:.2f}' if not np.isnan(n) else 'NaN' for n in all_ne_plot_units_std]}")
print(f"Mean Space Potential Vs (V): {[f'{s:.2f}' if not np.isnan(s) else 'NaN' for s in all_Vs_V_mean]}")
print(f"Std Dev Space Potential Vs (V): {[f'{s:.2f}' if not np.isnan(s) else 'NaN' for s in all_Vs_V_std]}")