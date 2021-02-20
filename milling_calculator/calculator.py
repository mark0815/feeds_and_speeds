from math import sin, sqrt, asin, pi
import typing as t


def calculate_rpm_vf(
    vc: float,
    fz: float,
    tool_diameter: float,
    tool_flute_count: int,
    max_rpm: float = None,
    max_vf: float = None,
) -> t.Tuple[float, float]:
    rpm = (vc * 1000) / (pi * tool_diameter)
    vf = rpm * fz * tool_flute_count

    if max_rpm and rpm > max_rpm:
        rpm = max_rpm
        vf = max_rpm * fz * tool_flute_count

    if max_vf and vf > max_vf:
        rpm = max_vf / (fz * tool_flute_count)
        vf = max_vf

    return (rpm, vf)


def avg_chip_thickness(
    ae: float,
    fz: float,
    tool_cutting_edge_angle: float,
    tool_diameter: float,
    phi: float,
) -> float:
    """ Average chip thickness hm """
    return (114.7 * fz * sin(tool_cutting_edge_angle) * (ae / tool_diameter)) / phi


def avg_cutting_force(kc_1_1: float, avg_chip_thickness: float, mc: float) -> float:
    """ Average cutting force (kc in N/mm^2) """
    return kc_1_1 / avg_chip_thickness ** mc


def chip_cross_section_per_tooth(avg_chip_thickness: float, ap: float) -> float:
    """ Cutting cross section per tooth (A in mm^2) """
    return ap * avg_chip_thickness


def cutting_force_per_tooth(
    avg_cutting_force: float, chip_cross_section_per_tooth: float
) -> float:
    """ Cutting force per tooth (Fc in N/mm^2) """
    return avg_cutting_force * chip_cross_section_per_tooth


def phi_by_selection(center_cut: bool, ae: float, tool_diameter: float) -> float:
    """ Calculated phi by selection based on ae """
    if center_cut:
        return 2 * asin(ae / tool_diameter)
    else:
        cutter_radius = tool_diameter / 2
        return 90 + asin((ae - cutter_radius) / cutter_radius)


def flutes_engaged(tool_diameter: float, phi: float) -> float:
    """ Number of flutes engaged in cut based on phi (Ze). """
    return tool_diameter * (phi / 360)


def zeit_span_volumen(ae: float, ap: float, vf: float) -> float:
    """ Q in cm^3 / min """
    return (ae * ap * vf) / 1000


def p_mot(q: float, kc: float) -> float:
    """ Pmot in Kw """
    mot_efficiency = 0.75
    return (q * kc) / (60000 * mot_efficiency)


def cutting_power(
    vc: float,
    kc_1_1: float,
    mc: float,
    center_cut: bool,
    ae: float,
    ap: float,
    tool_diameter: float,
    fz: float,
    tool_cutting_edge_angle: float,
) -> float:
    phi = phi_by_selection(center_cut=center_cut, ae=ae, tool_diameter=tool_diameter)
    avg_ct = avg_chip_thickness(
        ae=ae,
        fz=fz,
        tool_cutting_edge_angle=tool_cutting_edge_angle,
        tool_diameter=tool_diameter,
        phi=phi,
    )
    avg_cf = avg_cutting_force(kc_1_1=kc_1_1, avg_chip_thickness=avg_ct, mc=mc)
    ccspt = chip_cross_section_per_tooth(avg_chip_thickness=avg_ct, ap=ap)
    cfpt = cutting_force_per_tooth(
        avg_cutting_force=avg_cf, chip_cross_section_per_tooth=ccspt
    )
    f_eng = flutes_engaged(tool_diameter=tool_diameter, phi=phi)
    pm = (cfpt * f_eng * (vc / 60)) / 1000
    return pm


# NEU


def calc_n_spindle(v_c: float, d_c: float) -> float:
    """ Drehzahl in 1/min """
    return (v_c * 1000) / (d_c * pi)


def calc_v_f(f_z: float, z: int, n_spindle: float) -> float:
    """ Vorschubgeschwindigkeit in mm/min """
    return f_z * z * n_spindle


def calc_q(a_e: float, a_p: float, v_f: float) -> float:
    """ Zeitspanvolumen in cm^3/min """
    return (a_e * a_p * v_f) / 1000


def calc_p_mot(q: float, k_c: float) -> float:
    """ Leistungsbedarf Pmot in kW """
    n_machine = 0.75
    return (q * k_c) / (60000 * n_machine)


def calc_k_c(y: float, h_m: float, m_c: float, k_c_1_1: float) -> float:
    return ((1 - 0.01 * y) / h_m ** m_c) * k_c_1_1


def calc_h_m(f_z: float, k_apr: float, a_e: float, d_c: float, phi_s: float) -> float:
    """ Mittlere Spanungsdicke in mm """
    return (114.7 * f_z * sin(k_apr) * (a_e / d_c)) / phi_s


def calc_phi_s(mittig: bool, a_e: float, d_c: float) -> float:
    """ Eingriffswinkel in Grad (mittig/ausser-mittig) """
    if mittig:
        return 2 * asin(a_e / d_c)
    else:
        d_r = d_c / 2
        return 90 + asin((a_e - d_r) / d_r)


def calc_y(a_e: float, d_c: float) -> float:
    return a_e - (d_c / 2)


def final_pmot(
    mittig: bool,
    a_e: float,
    d_c: float,
    k_c_1_1: float,
    m_c: float,
    k_apr: float,
    f_z: float,
    a_p: float,
    z_cutter: int,
    v_c: float,
) -> float:
    phi_s = calc_phi_s(mittig=mittig, a_e=a_e, d_c=d_c)
    h_m = calc_h_m(f_z=f_z, k_apr=k_apr, a_e=a_e, d_c=d_c, phi_s=phi_s)
    y = calc_y(a_e=a_e, d_c=d_c)
    k_c = calc_k_c(y=y, k_c_1_1=k_c_1_1, m_c=m_c, h_m=h_m)
    n_spindle = calc_n_spindle(v_c=v_c, d_c=d_c)
    v_f = calc_v_f(f_z=f_z, z=z_cutter, n_spindle=n_spindle)
    q = calc_q(a_e=a_e, a_p=a_p, v_f=v_f)
    p_mot = calc_p_mot(q=q, k_c=k_c)
    return p_mot
