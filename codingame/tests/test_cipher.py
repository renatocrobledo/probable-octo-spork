from src import cipher
from tests import mock_input

def inyect_and_run(inputs, result):
    mock_input.inyect(inputs, cipher.encode, result)


def test_all():
    
    _input = ['i am a programmer','ab']
    _output = 'i bm b psohrbmnes'
    inyect_and_run(_input,_output)

    _input = ['the presidential ceremony will be held tomorrow at 10','invalid']
    _output = 'buz pcmvqqzneqdt pzrpurvl riwt em uzlo brubmrze db 10'
    inyect_and_run(_input,_output)

    _input = ['the president has to decided to cancel all the upcoming meetings until further notice','parliament']
    _output = 'ihv azeemqxct yla ta hrvxdvo bo oeavtl rwt tti hirodtvg yirmxnxd cnfmy yjrksmr zsgbre'
    inyect_and_run(_input,_output)

    _input = ['i don t know what i am going to do','ab']
    _output = 'i eoo t lnpw xhbt j an gpiog uo eo'
    inyect_and_run(_input,_output)
