d = {
    'test'                : ['Diboson_ww'],

    'MET'                 : ['MET'],
    'SingleElectron'      : ['SingleElectron'],
    'SingleMuon'          : ['SingleMuon'],
    'DoubleEG'            : ['DoubleEG'],
    'SinglePhoton'        : ['SinglePhoton'],

    'Diboson'             : ['Diboson_ww','Diboson_wz','Diboson_zz'],
    'SingleTop'           : ['SingleTop_tT','SingleTop_tTbar','SingleTop_tbarW','SingleTop_tW',
                             'SingleTop_tZll','SingleTop_tZnunu'],
    'SingleTop_tG'        : ['SingleTop_tG'],
    'TTbar'               : ['TTbar_Powheg'],
    'TTbar_L'             : ['TTbar_1LT','TTbar_1LTbar'],
    'TTbar_2L'            : ['TTbar_2L'],
    'TTbar_isrup'         : ['TTbar_PowhegISRUp'],
    'TTbar_isrdown'       : ['TTbar_PowhegISRDown'],
    'TTbar_tuneup'        : ['TTbar_PowhegTuneUp'],
    'TTbar_tunedown'      : ['TTbar_PowhegTuneDown'],
    'TTbar_FXFX'          : ['TTbar_FXFX'],
    'TTbar_Herwig'        : ['TTbar_Herwig'],
    'TTbar_Photon'        : ['TTbar_GJets'],
    'QCD'                 : ['QCD_ht100to200','QCD_ht200to300','QCD_ht300to500','QCD_ht500to700',
                              'QCD_ht700to1000','QCD_ht1000to1500','QCD_ht1500to2000','QCD_ht2000toinf'],

    'ZHbb'                : ['ZHbb_mH125'],
    'ggZHbb'              : ['ggZHbb_mH125'],
    'ggHbb'               : ['ggHbb_mH125'],
    'ttHbb'               : ['ttHbb_mH125'],
    'VBFHbb'              : ['VBFHbb_mH125'],
    'WpH'                 : ['WpLNuHbb'],
    'WmH'                 : ['WmLNuHbb'],

    'GJets'               : ['GJets_ht100to200','GJets_ht200to400','GJets_ht400to600','GJets_ht600toinf'],
    'WJets'               : ['WJets_ht100to200','WJets_ht200to400','WJets_ht400to600','WJets_ht600to800',
                             'WJets_ht800to1200','WJets_ht1200to2500','WJets_ht2500toinf'],
    'WJets_nlo'           : ['WJets_pt%sto%s'%(str(x[0]),str(x[1])) for x in 
                             [(100,250),(250,400),(400,600),(600,'inf')] ],
    'ZJets'               : ['ZJets_ht%sto%s'%(str(x[0]),str(x[1])) for x in 
                                [(100,200),(200,400),(400,600),(600,800),(800,1200),(1200,2500),(2500,'inf')]],
    'ZJets_nlo'           : ['ZJets_pt%sto%s'%(str(x[0]),str(x[1])) for x in 
                             [(50,100),(100,250),(250,400),(400,650),(650,'inf')] ],
    'ZtoNuNu'             : ['ZtoNuNu_ht100to200','ZtoNuNu_ht200to400','ZtoNuNu_ht400to600',
                             'ZtoNuNu_ht600to800','ZtoNuNu_ht800to1200','ZtoNuNu_ht1200to2500',
                             'ZtoNuNu_ht2500toinf'],
    'ZtoNuNu_nlo'         : ['ZtoNuNu_pt%sto%s'%(str(x[0]),str(x[1])) for x in 
                             [(100,250),(250,400),(400,650),(650,'inf')] ],

    'ZpTT'                : ['ZpTT_med-%i'%m for m in [1000,1250,1500,2000,2500,3000,3500,4000,500,750]],
    'ZpWW'                : ['ZpWW_med-%i'%m for m in [1000,1200,1400,1600,1800,2000,2500,800]],
    'ZpA0h'               : ['ZpA0h_med-%i_dm-%i'%m for m in 
                             [(1000,300), (1000,400), (1000,500), (1000,600), (1000,700), (1000,800), 
                              (1200,300), (1200,400), (1200,500), (1200,600), (1200,700), (1200,800), 
                              (1400,300), (1400,400), (1400,500), (1400,600), (1400,700), (1400,800), 
                              (1700,300), (1700,400), (1700,500), (1700,600), (1700,700), (1700,800), 
                              (2000,300), (2000,400), (2000,500), (2000,600), (2000,700), (2000,800), 
                              (2500,300), (2500,400), (2500,500), (2500,600), (2500,700), (2500,800), 
                              (600,300), (600,400), (800,300), (800,400), (800,500), (800,600)]
                            ],
    'DiJetsDM'            : ['DiJetsDM_MZprime-%i_Mhs-%i_Mchi-10'%m for m in 
                             [(1000,150), (1000,50), (100,150), (100,50), (1500,150), (1500,50), 
                              (2000,150), (2000,50), (2500,150), (2500,50), (3000,150), (3000,50), 
                              (300,150), (300,50), (500,150), (500,50), (50,150), (50,50)] 
                            ],
    'BBbarDM'             : ['BBbarDM_MZprime-%i_Mhs-%i_Mchi-%i'%m for m in 
                             [(1000,50,100), (1000,50,150), (1000,50,200), (1000,50,250), (1000,50,50), (1000,90,100), 
                              (1000,90,150), (1000,90,250), (1000,90,300), (1000,90,400), (1000,90,50), (1500,50,100), 
                              (1500,50,150), (1500,50,200), (1500,50,250), (1500,50,300), (1500,50,400), (1500,50,50), 
                              (1500,90,100), (1500,90,150), (1500,90,200), (1500,90,250), (1500,90,300), (1500,90,400), 
                              (1500,90,50), (2000,50,100), (2000,50,150), (2000,50,200), (2000,50,250), (2000,50,300), 
                              (2000,50,400), (2000,50,50), (2000,90,100), (2000,90,150), (2000,90,200), (2000,90,250), 
                              (2000,90,300), (2000,90,400), (2000,90,50), (2500,50,100), (2500,50,150), (2500,50,200), 
                              (2500,50,250), (2500,50,300), (2500,50,400), (2500,50,50), (2500,90,100), (2500,90,150), 
                              (2500,90,200), (2500,90,250), (2500,90,300), (2500,90,400), (2500,90,50), (3000,50,100), 
                              (3000,50,150), (3000,50,200), (3000,50,250), (3000,50,300), (3000,50,400), (3000,50,50), 
                              (3000,70,100), (3000,70,150), (3000,70,200), (3000,70,250), (3000,70,300), (3000,70,400), 
                              (3000,70,50), (3000,90,100), (3000,90,150), (3000,90,200), (3000,90,250), (3000,90,300), 
                              (3000,90,400), (3000,90,50), (495,50,250), (495,70,250), (495,90,250), (500,50,100), 
                              (500,50,150), (500,50,200), (500,50,50), (500,90,100), (500,90,150), (500,90,200), 
                              (500,90,50)]
                            ],
    'Monotop'             : ['Vector_MonoTop_Leptonic_Mphi_%i_Mchi_%i'%m for m in 
                             [(1000,1000), (1000,1), (1000,200), (1000,490), (1500,1000), (1500,1), 
                              (1500,200), (1500,500), (1750,1000), (1750,1), (1750,200), (1750,500), 
                              (2000,1), (2000,200), (2000,500), (2000,990), (2250,1), (2500,1000), 
                              (2500,1), (2500,200), (2500,500), (300,1000), (300,1), (300,200), 
                              (300,500), (500,1000), (500,1), (500,500), (750,1000), (750,1), 
                              (750,200), (750,500)]
                            ],
}
