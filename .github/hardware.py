from enum import Enum


class FieldType(Enum):
    PIN = 0
    INT = 1
    BOOL = 2
    FLOAT = 3
    ARRAY = 4
    COUNT = 5


hardware_fields = {
    "serial_rx": FieldType.PIN,
    "serial_tx": FieldType.PIN,
    "radio_busy": FieldType.PIN,
    "radio_busy_2": FieldType.PIN,
    "radio_dio0": FieldType.PIN,
    "radio_dio0_2": FieldType.PIN,
    "radio_dio1": FieldType.PIN,
    "radio_dio1_2": FieldType.PIN,
    "radio_dio2": FieldType.PIN,
    "radio_miso": FieldType.PIN,
    "radio_mosi": FieldType.PIN,
    "radio_nss": FieldType.PIN,
    "radio_nss_2": FieldType.PIN,
    "radio_rst": FieldType.PIN,
    "radio_rst_2": FieldType.PIN,
    "radio_sck": FieldType.PIN,
    "radio_dcdc": FieldType.BOOL,
    "radio_rfo_hf": FieldType.BOOL,
    "ant_ctrl": FieldType.PIN,
    "ant_ctrl_compl": FieldType.PIN,
    "power_enable": FieldType.PIN,
    "power_apc1": FieldType.PIN,
    "power_apc2": FieldType.PIN,
    "power_rxen": FieldType.PIN,
    "power_txen": FieldType.PIN,
    "power_rxen_2": FieldType.PIN,
    "power_txen_2": FieldType.PIN,
    "power_lna_gain": FieldType.INT,
    "power_min": FieldType.INT,
    "power_high": FieldType.INT,
    "power_max": FieldType.INT,
    "power_default": FieldType.INT,
    "power_pdet": FieldType.PIN,
    "power_pdet_intercept": FieldType.FLOAT,
    "power_pdet_slope": FieldType.FLOAT,
    "power_control": FieldType.INT,
    "power_values": FieldType.ARRAY,
    "power_values2": FieldType.ARRAY,
    "power_values_dual": FieldType.ARRAY,
    "joystick": FieldType.PIN,
    "joystick_values": FieldType.ARRAY,
    "five_way1": FieldType.PIN,
    "five_way2": FieldType.PIN,
    "five_way3": FieldType.PIN,
    "button": FieldType.PIN,
    "button_led_index": FieldType.INT,
    "button2": FieldType.PIN,
    "button2_led_index": FieldType.INT,
    "led": FieldType.PIN,
    "led_blue": FieldType.PIN,
    "led_blue_invert": FieldType.BOOL,
    "led_green": FieldType.PIN,
    "led_green_invert": FieldType.BOOL,
    "led_green_red": FieldType.PIN,
    "led_red": FieldType.PIN,
    "led_red_invert": FieldType.BOOL,
    "led_red_green": FieldType.PIN,
    "led_rgb": FieldType.PIN,
    "led_rgb_isgrb": FieldType.BOOL,
    "ledidx_rgb_status": FieldType.ARRAY,
    "ledidx_rgb_status_count": FieldType.COUNT,
    "ledidx_rgb_vtx": FieldType.ARRAY,
    "ledidx_rgb_vtx_count": FieldType.COUNT,
    "ledidx_rgb_boot": FieldType.ARRAY,
    "ledidx_rgb_boot_count": FieldType.COUNT,
    "screen_cs": FieldType.PIN,
    "screen_dc": FieldType.PIN,
    "screen_mosi": FieldType.PIN,
    "screen_rst": FieldType.PIN,
    "screen_sck": FieldType.PIN,
    "screen_sda": FieldType.PIN,
    "screen_type": FieldType.INT,
    "screen_reversed": FieldType.BOOL,
    "screen_bl": FieldType.PIN,
    "use_backpack": FieldType.BOOL,
    "debug_backpack_baud": FieldType.INT,
    "debug_backpack_rx": FieldType.PIN,
    "debug_backpack_tx": FieldType.PIN,
    "backpack_boot": FieldType.PIN,
    "backpack_en": FieldType.PIN,
    "passthrough_baud": FieldType.INT,
    "i2c_scl": FieldType.PIN,
    "i2c_sda": FieldType.PIN,
    "misc_gsensor_int": FieldType.PIN,
    "misc_buzzer": FieldType.PIN,
    "misc_fan_en": FieldType.PIN,
    "misc_fan_pwm": FieldType.PIN,
    "misc_fan_tacho": FieldType.PIN,
    "misc_fan_speeds": FieldType.ARRAY,
    "misc_fan_speeds_count": FieldType.COUNT,
    "gsensor_stk8xxx": FieldType.BOOL,
    "thermal_lm75a": FieldType.BOOL,
    "pwm_outputs": FieldType.ARRAY,
    "pwm_outputs_count": FieldType.COUNT,
    "vbat": FieldType.PIN,
    "vbat_offset": FieldType.INT,
    "vbat_scale": FieldType.INT,
    "vbat_atten": FieldType.INT,
    "vtx_amp_pwm": FieldType.PIN,
    "vtx_amp_vpd": FieldType.PIN,
    "vtx_amp_vref": FieldType.PIN,
    "vtx_nss": FieldType.PIN,
    "vtx_miso": FieldType.PIN,
    "vtx_mosi": FieldType.PIN,
    "vtx_sck": FieldType.PIN,
    "vtx_amp_vpd_25mW": FieldType.ARRAY,
    "vtx_amp_vpd_100mW": FieldType.ARRAY
}


def validate(target, layout):
    had_error = False
    # Ensure that all fields in the layout are valid fields from the hardware list
    for field in layout:
        if field not in hardware_fields.keys():
            print(f'device "{target}" has an unknown field name {field}')
            had_error = True
    #
    return had_error
