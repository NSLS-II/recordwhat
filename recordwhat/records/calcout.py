from collections import OrderedDict
from ophyd import (EpicsSignal, EpicsSignalRO, Device,
                   DynamicDeviceComponent as DDC)

from .. import (RecordBase, _register_record_type,
                FieldComponent as Cpt,
                FormattedFieldComponent as FCpt)


class CalcoutInput(Device):
    previous_value = FCpt(EpicsSignalRO, '{self.prefix}.L{self.input_name}')
    value = FCpt(EpicsSignalRO, '{self.prefix}.{self.input_name}')
    link = FCpt(EpicsSignalRO, '{self.prefix}.INP{self.input_name}$',
                string=True)
    status = FCpt(EpicsSignalRO, '{self.prefix}.IN{self.input_name}V')

    def __init__(self, prefix='', *, input_name, **kwargs):
        self.input_name = input_name
        super().__init__(prefix, **kwargs)


def _make_inputs(input_names, cls=CalcoutInput):
    return OrderedDict(('input_{}'.format(inp.lower()),
                        (cls, '', dict(input_name=inp)))
                       for inp in input_names)


@_register_record_type('calcout')
class CalcoutRecord(RecordBase):
    inputs = DDC(_make_inputs('ABCDEFGHIJKL'))

    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    calc_valid = Cpt(EpicsSignal, '.CLCV')
    last_val_monitored = Cpt(EpicsSignalRO, '.MLST')
    last_value_alarmed = Cpt(EpicsSignalRO, '.LALM')
    last_value_archived = Cpt(EpicsSignalRO, '.ALST')
    ocal_valid = Cpt(EpicsSignal, '.OCLV')
    out_pv_status = Cpt(EpicsSignalRO, '.OUTV')
    output_delay_active = Cpt(EpicsSignalRO, '.DLYA')
    output_value = Cpt(EpicsSignal, '.OVAL')
    prev_value_of_oval = Cpt(EpicsSignal, '.POVL')
    previous_value = Cpt(EpicsSignal, '.PVAL')

    # - alarms
    alarm_deadband = Cpt(EpicsSignal, '.HYST')
    high_alarm_limit = Cpt(EpicsSignal, '.HIGH')
    high_severity = Cpt(EpicsSignal, '.HSV')
    hihi_alarm_limit = Cpt(EpicsSignal, '.HIHI')
    hihi_severity = Cpt(EpicsSignal, '.HHSV')
    lolo_alarm_limit = Cpt(EpicsSignal, '.LOLO')
    lolo_severity = Cpt(EpicsSignal, '.LLSV')
    low_alarm_limit = Cpt(EpicsSignal, '.LOW')
    low_severity = Cpt(EpicsSignal, '.LSV')
    output_execute_delay = Cpt(EpicsSignal, '.ODLY')

    # - calc
    calculation = Cpt(EpicsSignal, '.CALC$', string=True)
    output_calculation = Cpt(EpicsSignal, '.OCAL$', string=True)
    output_data_opt = Cpt(EpicsSignal, '.DOPT')
    output_execute_opt = Cpt(EpicsSignal, '.OOPT')

    # - clock
    event_to_issue = Cpt(EpicsSignal, '.OEVT')

    # - display
    archive_deadband = Cpt(EpicsSignal, '.ADEL')
    display_precision = Cpt(EpicsSignal, '.PREC')
    high_operating_rng = Cpt(EpicsSignal, '.HOPR')
    low_operating_range = Cpt(EpicsSignal, '.LOPR')
    monitor_deadband = Cpt(EpicsSignal, '.MDEL')
    units_name = Cpt(EpicsSignal, '.EGU$', string=True)

    # - output
    invalid_output_action = Cpt(EpicsSignal, '.IVOA')
    invalid_output_value = Cpt(EpicsSignal, '.IVOV')
    output_specification = Cpt(EpicsSignal, '.OUT$', string=True)
