from ophyd import (EpicsSignal, EpicsSignalRO, Component as Cpt)

from .. import (RecordBase, _register_record_type)


@_register_record_type('timestamp')
class TimestampRecord(RecordBase):
    _rtyp = 'timestamp'
    alarm_status = Cpt(EpicsSignalRO, '.STAT')
    current_raw_value = Cpt(EpicsSignal, '.RVAL')
    previous_value = Cpt(EpicsSignalRO, '.OVAL')

    # - inputs
    time_stamp_type = Cpt(EpicsSignal, '.TST')