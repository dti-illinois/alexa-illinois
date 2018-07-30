class EWSConsts:

    DCL_name = 'digital computer lab'
    ECE_name = 'electrical and computer engineering building'
    EH_name = 'engineering hall'
    GELIB_name = 'grainger engineering library'
    MEL_name = 'mechanical engineering lab'
    SIEBL_name = 'siebel center'
    TB_name = 'transportation building'

    dummy_building_list = ['FAR', 'ESPL', 'PAR', 'REC', 'SDRP']

    inuse_building_list = [DCL_name, ECE_name, EH_name, GELIB_name, MEL_name, SIEBL_name, TB_name]

    buildings = {
        #DCL
        'DCL': DCL_name,
        'dcl': DCL_name,
        'digital computer lab': DCL_name,
        'digital computer laboratory': DCL_name,
        #ECEBuidling
        'ECEB': ECE_name,
        'ece': ECE_name,
        'eceb': ECE_name,
        'ece building': ECE_name,
        'electrical and computer engineering building': ECE_name,
        #EH
        'EH': EH_name,
        'eh': EH_name,
        'engineering hall': EH_name,
        #GELIB
        'GELIB': GELIB_name,
        'gelib': GELIB_name,
        'grainger': GELIB_name,
        'grainger library': GELIB_name,
        'grainger engineering library': GELIB_name,
        #MEL
        'MEL': MEL_name,
        'mel': MEL_name,
        'mechanical lab': MEL_name,
        'mechanical engineering lab': MEL_name,
        'mechanical engineering laboratory': MEL_name,
        #SIEBL
        'SIEBL': SIEBL_name,
        'siebl': SIEBL_name,
        'siebel': SIEBL_name,
        'siebel center': SIEBL_name,
        #TB
        'TB': TB_name,
        'tb': TB_name,
        'transportation building': TB_name
    }

    rooms = {
        #room for DCL
        '416': 'L416',
        '426': 'L426',
        '440': 'L440',
        '520': 'L520',
        #room for TB
        '207': '207',
        '302': '302',
        '316': '316',
        #room for ECEB
        '2022': '2022',
        '3022': '3022',
        '3070': '3070',
        #room for EH
        '4061': '406B1',
        '4068': '406B8',
        '406B1': '406B1',
        '406B8': '406B8',
        #room for MEL
        '1001': '1001',
        '1009': '1009',
        #room for siebel
        '0218': '0218',
        '0220': '0220',
        '0222': '0222',
        '0403': '0403',
        '218': '0218',
        '220': '0220',
        '222': '0222',
        '403': '0403',
        #room for GELIB
        'fourth floor center': 'fourth floor center',
        'fourth floor east': 'fourth floor east',
        '4th floor center': 'fourth floor center',
        '4th floor east': 'fourth floor east'
    }

class ICSConsts:

    ALN_name = 'allen residence hall'
    BEH_name = 'busey evans'
    DAN_name = 'daniels'
    ENG_name = 'english'
    FAR_name = 'florida avenue'
    IH_name = 'illini hall'
    IKE_name = 'ikenberry floor one'
    IKE2_name = 'ikenberry floor two'
    ISR_name = 'illinois street'
    NEV_name = 'nevada'
    OR_name = 'oregon'
    ORC_name = 'orchard downs'
    PAR_name = 'pennsylvania avenue'
    SHM_name = 'sherman'
    UG_name = 'undergrad'
    UN_name = 'illini union'
    WH_name = 'wohlers'

    dummy_building_list = ['AUO', 'BOU', 'CLK', 'GNG', 'HOP', 'NUG', 'SCT', 'SDRPH', 'SNY', 'TRE', 'TVD', 'WAS', 'WSH']

    inuse_building_list = [ALN_name, BEH_name, DAN_name, ENG_name, FAR_name, IH_name, IKE_name, IKE2_name, ISR_name,
                            NEV_name, OR_name, ORC_name, PAR_name, SHM_name, UG_name, UN_name, WH_name]

    buildings = {
        'aln': ALN_name,
        'allen residence hall': ALN_name,
        'beh': BEH_name,
        'busey evans': BEH_name,
        'dan': DAN_name,
        'daniels': DAN_name,
        'eng': ENG_name,
        'english': ENG_name,
        'far': FAR_name,
        'florida avenue': FAR_name,
        'ih23': IH_name,
        'illini hall': IH_name,
        'ike': IKE_name,
        'ikenberry floor one': IKE_name,
        'ikenberry floor 1': IKE_name,
        'ike2': IKE2_name,
        'ikenberry floor two': IKE2_name,
        'ikenberry floor 2': IKE2_name,
        'isr': ISR_name,
        'illinois street': ISR_name,
        'nev': NEV_name,
        'nevada': NEV_name,
        'or': OR_name,
        'oregon': OR_name,
        'orc': ORC_name,
        'orchard downs': ORC_name,
        'par': PAR_name,
        'pennsylvania avenue': PAR_name,
        'shm': SHM_name,
        'sherman': SHM_name,
        'ug': UG_name,
        'undergrad': UG_name,
        'un': UN_name,
        'illini union': UN_name,
        'wh': WH_name,
        'wohlers': WH_name
    }
