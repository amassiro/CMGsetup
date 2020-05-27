Compare chargino samples
====


/AMSB_chargino_M-*_CTau-*_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER 
dataset=/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step3-03e52fcf90ac03c0e0d2278157727e12/USER
dataset=/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step2-5b9cd2c7eef36524de7af1c8e43b0ebc/USER
dataset=/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-1de02c2fd139009e4ede1c745c02b544/USER

    cmsRun gendumper_cfg.py   inputFiles=/store/user/ahart/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1/190103_131057/0000/AMSB_chargino600GeV_ctau10cm_step1_98.root  \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

file dataset=/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-1de02c2fd139009e4ede1c745c02b544/USER


    cmsRun gendumper_cfg.py   inputFiles=/store/user/ahart/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1/190103_131057/0000/AMSB_chargino600GeV_ctau10cm_step1_186.root \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


file dataset=/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step2-5b9cd2c7eef36524de7af1c8e43b0ebc/USER

    cmsRun gendumper_cfg.py   inputFiles=/store/user/ahart/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step2/190104_142631/0000/AMSB_chargino700GeV_ctau100cm_step2_98.root \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 



file dataset=/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step3-03e52fcf90ac03c0e0d2278157727e12/USER

    cmsRun gendumper_cfg.py   inputFiles=/store/user/ahart/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step3/190105_134437/0000/AMSB_chargino700GeV_ctau100cm_step3_98.root \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 



file dataset=/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4-0a25f51d323b7ece21362186c9e91a1a/USER


    cmsRun gendumper_cfg.py   inputFiles=/store/user/ahart/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step4/190107_111025/0000/AMSB_chargino700GeV_ctau100cm_step4_98.root \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    cmsRun gendumper_cfg.py   inputFiles=many::samples_private_500GeV_10cm_Ohio.py \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
                              
To Run:
====

    cd /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/27Feb2020/CMSSW_10_4_0/src/LatinoTreesGEN/GenDumper/test
    
    cmsenv
    
    voms-proxy-init --voms cms -rfc


    cmsRun gendumper_cfg.py   inputFiles=many::samples_private_500GeV_10cm_Ohio.py \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=many::samples_500GeV10cm_noFilter.py  \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=many::samples_private_500GeV_10cm_metcut.py  \
                              outputFile=/tmp/amassiro/private_500GeV_10cm.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG.py  \
                              outputFile=/tmp/amassiro/petrucciani_500GeV_10cm.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=many::samples_600GeV10cm.py  \
                              outputFile=/tmp/amassiro/private_600GeV_10cm.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 
                          

                          
Measure gen met cut efficiency


    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,2000,\"1\",0,1.0,1.0\) 
           
    From the ratio plot: 0.13157895
           
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,2000,\"1\",0,1.0,0.13157895\) 
           
           

Plot
====


    ls -alrth /eos/cms/store/group/phys_susy/xtracks/500GeV10cm/miniAOD-PU/c* | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_private_500GeV_10cm_metcut.py

    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_500_cTau_10.merged/W* | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG.py

    
    
    
    r99t   /tmp/amassiro/petrucciani_500GeV_10cm.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",20,0,500,\"1\",0\) 
    
    
    r99t   /tmp/amassiro/petrucciani_500GeV_10cm.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,1000,\"1\",0,1.0,0.135\) 

    r99t   /tmp/amassiro/petrucciani_500GeV_10cm.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",4,0,600,\"1\",0,1.0,0.135\) 

           
    r99t   /tmp/amassiro/petrucciani_500GeV_10cm.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"jetpt1\",30,0,1000,\"genMetTrue\>150\",0,1.0,1.0\) 

    r99t   /tmp/amassiro/petrucciani_500GeV_10cm.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"jetpt2\",30,0,300,\"genMetTrue\>150\",0,1.0,1.0\) 
           
           
    r99t   /tmp/amassiro/petrucciani_500GeV_10cm.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"std_vector_CharginoGen_pt[0]\",20,0,1000,\"1\",0,1.0,0.135\) 

    r99t   /tmp/amassiro/petrucciani_500GeV_10cm.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"std_vector_CharginoGen_pt[0]\",15,0,2000,\"genMetTrue\>150\",0,1.0,1.0\) 
       
    
           
           
           
    cmsRun gendumper_cfg.py   inputFiles=/store/group/phys_susy/xtracks/500GeV10cm_noFilter/miniAOD/chargino500GeV_ctau10cm_miniAOD_144.root  \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    ls -alrth /eos/cms/store/group/phys_susy/xtracks/500GeV10cm_noFilter/miniAOD/c* | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_500GeV10cm_noFilter.py

    cmsRun gendumper_cfg.py   inputFiles=many::samples_500GeV10cm_noFilter.py  \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
                              
    
    
    /eos/cms/store/group/phys_susy/xtracks/600GeV10cm/miniAOD-PU
                              
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/600GeV10cm/miniAOD-PU/c* | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_600GeV10cm.py

    cmsRun gendumper_cfg.py   inputFiles=many::samples_600GeV10cm.py  \
                              outputFile=/tmp/amassiro/private_600GeV_10cm.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 
                              
    
    
    
    
                              
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,1000,\"1\",0,1.0,0.135\)        
           
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,1000,\"1\",0,1.0,1.0\) 
           
           
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",160,0,2000,\"1\",0,1.0,1.0\) 

    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",1000,0,1000,\"1\",0,1.0,1.0\) 

           
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"std_vector_CharginoGen_pt[0]\",15,0,2000,\"genMetTrue\>150\",0,1.0,1.0\) 

           
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"std_vector_CharginoGen_pt[0]\",15,0,2000,\"1\",0,1.0,1.0\) 

    
     sqrt\(
     \(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)*
     \(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)+
     \(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)*
     \(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)
     \)
    
     sqrt\(\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)+\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)\)
     
     r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"sqrt\(\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)+\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)\)\",60,0,3000,\"@std_vector_CharginoGen_pt.size\(\)\>1\",0,1.0,1.0\) 

           
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"sqrt\(\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)+\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)\)\",60,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\>1\)\&\&\(genMetTrue\>150\)\",0,1.0,1.0\) 
       
     
     
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"sqrt\(\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)+\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)\)\",60,0,3000,\"@std_vector_CharginoGen_pt.size\(\)\>1\",0,1.0,1.0\) 

    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"sqrt\(\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*cos\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*cos\(std_vector_CharginoGen_phi[1]\)\)+\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)*\(std_vector_CharginoGen_pt[0]*sin\(std_vector_CharginoGen_phi[0]\)+std_vector_CharginoGen_pt[1]*sin\(std_vector_CharginoGen_phi[1]\)\)\)\",60,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\>1\)\&\&\(genMetTrue\>150\)\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"diCharginoPT\",60,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\>1\)\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"diCharginoPT\",60,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\=\=2\)\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"diCharginoPT\",60,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\=\=2\)\",0,1.0,1.0\) 
    
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"diCharginoPT\",60,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\=\=1\)\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"diCharginoPT\",200,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\=\=2\)\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"diCharginoPT\",200,0,3000,\"1\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"\(@std_vector_CharginoGen_pt.size\(\)\)\",10,0,10,\"1\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"\(@std_vector_CharginoGen_pt.size\(\)\)\",30,0,30,\"1\",0,1.0,1.0\) 
    
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"\(abs\(std_vector_CharginoGen_id\)\=\=1000024\)\+2\*\(abs\(std_vector_CharginoGen_id\)\=\=1000037\)\",8,0,4,\"\(@std_vector_CharginoGen_pt.size\(\)\>0\)\",0,1.0,1.0\) 
     
    1000024 || 1000037
    
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"\std_vector_CharginoGen_status\",100,0,100,\"\(@std_vector_CharginoGen_pt.size\(\)\>0\)\",0,1.0,1.0\) 
     
     
     
     
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"\(@std_vector_CharginoGen_pt.size\(\)\)\",10,0,10,\"1\",0,1.0,1.0\) 
     
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"\(@std_vector_CharginoGen_pt.size\(\)\)\",10,0,10,\"1\",0,1.0,1.0\) 
          
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"std_vector_CharginoGen_pt[0]\",100,0,400,\"1\",0,1.0,1.0\) 
    
    
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"diCharginoPT\",60,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\>1\)\&\&\(genMetTrue\>150\)\",0,1.0,1.0\) 
    
    
    
      
      
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"\(std_vector_CharginoGen_status[0]\)\",100,-50,50,\"1\",0,1.0,1.0\) 
      
      
      
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,1000,\"1\",0,1.0,1.0\) 

    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,1000,\"1\",0,1.0,1.0\) 
           
    
     chargino-pair pt for two-track events
     chargino-neutralino pair pt for single track events
     
       
       
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"\(@std_vector_CharginoGen_pt.size\(\)\)\",10,0,10,\"1\",0,1.0,1.0\) 
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"\(@std_vector_CharginoGen_pt.size\(\)\)\",30,0,30,\"1\",0,1.0,1.0\) 
           
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"diCharginoPT\",200,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\=\=2\)\",0,1.0,1.0\) 
    
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"diCharginoPT\",200,0,3000,\"\(@std_vector_CharginoGen_pt.size\(\)\=\=2\)\",0,1.0,1.0\) 
    
    
    
Gen weights from Ohio 

    wget https://github.com/OSU-CMS/DisappTrks/raw/master/StandardAnalysis/data/isrWeight_disappTrks_run2.root
    
    
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_Ohio.root           \
           DrawCompare.cxx\(\"genMetTrue\",40,0,1000,\"1\",0,1.0,1.0\) 


    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_nomet.root           \
           DrawCompareWithWeight.cxx\(\"genMetTrue\",40,0,1000,\"1\",0,1.0,1.0\) 


    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_nomet.root           \
           DrawCompareWithWeight.cxx\(\"genMetTrue\",1000,0,1000,\"1\",0,1.0,1.0\) 

     
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_nomet.root           \
           DrawCompareWithWeight.cxx\(\"new_diCharginoPT\",100,0,1000,\"1\",0,1.0,1.0\) 
    
    
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/private_500GeV_10cm_nomet.root           \
           DrawCompareWithWeight.cxx\(\"new_diCharginoPT\",500,0,500,\"1\",0,1.0,1.0\) 
    
      
    r99t   /tmp/amassiro/private_500GeV_10cm_nomet.root       \
           /tmp/amassiro/petrucciani_500GeV_10cm.root           \
           DrawCompare.cxx\(\"genMetTrue\",1000,0,1000,\"1\",0,1.0,1.0\) 

    hadd hratio_together.root hratio_cmg.root hratio.root
    
    output: /afs/cern.ch/user/a/amassiro/public/xJeremiNiedziela/hratio_together.root
            /afs/cern.ch/user/a/amassiro/public/xJeremiNiedziela/hratio_together_newName.root
    
           
Produce trees:

    cmsRun gendumper_cfg.py   inputFiles=many::samples_500GeV10cm_noFilter.py  \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=many::samples_private_500GeV_10cm_Ohio.py \
                              outputFile=/tmp/amassiro/private_500GeV_10cm_Ohio.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


Origin:

    https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/plugins/ISRWeightProducer.cc#L71

    
The electroweakinos "of interest" would be, in Pythia8, the "isLastCopy && !isFirstCopy" (with "statusFlags().") 1000024 and 1000022 GenParticles -- this is because Pythia8 does not boost from ISR the first copies. Also a first copy could be a neutralino from a chargino's decay, and you don't want to add that momentum twice.

With that pair-pt just evaluate both the madgraph/pythia8 and data/MC histograms, and weight your events with the product of those bin values.

    2017 conditions: "SingleMu_2017" and "madgraphOverPythia8_94X"
    2018 conditions: "SingleMu_2018" and "madgraphOverPythia8_102X"













Extract efficiency for differen masses
====

    cd /afs/cern.ch/user/a/amassiro/work/CMG/DisappearingTracks/27Feb2020/CMSSW_10_4_0/src/LatinoTreesGEN/GenDumper/test
    
    cmsenv
    
    voms-proxy-init --voms cms -rfc


#     M=300, 1cm production (with MET filter at 150 GeV):
#    /eos/cms/store/group/phys_susy/xtracks/300GeV1cm_2017/miniAOD
#    
#    M=300, 30cm production (with MET filter at 150 GeV):
#    /eos/cms/store/group/phys_susy/xtracks/300GeV30cm_2017/miniAOD
#    
#    M=900, 1cm production (with MET filter at 150 GeV):
#    /eos/cms/store/group/phys_susy/xtracks/900GeV1cm_2017/miniAOD
#    
#    M=900, 30 cm production (with MET filter at 150 GeV):
#    /eos/cms/store/group/phys_susy/xtracks/900GeV30cm_2017/miniAOD
#    
#    M=500, 1cm production (with MET filter at 150 GeV):
#    /eos/cms/store/group/phys_susy/xtracks/500GeV1cm_2017/miniAOD
#    
#    M=500, 10cm production (with MET filter at 150 GeV)
#    /eos/cms/store/group/phys_susy/xtracks/500GeV10cm_newGT/miniAOD
#    


 /eos/cms/store/group/phys_susy/xtracks/300GeV1cm_2017/miniAOD
 /eos/cms/store/group/phys_susy/xtracks/500GeV1cm_2017/miniAOD
 /eos/cms/store/group/phys_susy/xtracks/900GeV1cm_2017/miniAOD
 /eos/cms/store/group/phys_susy/xtracks/300GeV30cm_2017/miniAOD
 /eos/cms/store/group/phys_susy/xtracks/900GeV30cm_2017/miniAOD
 
 
 
 
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/300GeV1cm_2017/miniAOD/c*   | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_300GeV1cm_2017.py
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/500GeV1cm_2017/miniAOD/c*   | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_500GeV1cm_2017.py
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/900GeV1cm_2017/miniAOD/c*   | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_900GeV1cm_2017.py
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/900GeV30cm_2017/miniAOD/c*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_900GeV30cm_2017.py
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/300GeV10cm_2017/miniAOD/c*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_300GeV10cm_2017.py
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/900GeV10cm_2017/miniAOD/c*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_900GeV10cm_2017.py
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/500GeV30cm_2017/miniAOD/c*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_500GeV30cm_2017.py
    ls -alrth /eos/cms/store/group/phys_susy/xtracks/300GeV30cm_2017/miniAOD/c*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_Py_300GeV30cm_2017.py

    ls -alrth /eos/cms/store/group/phys_susy/xtracks/300GeV1cm/miniAOD-PU/c*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_TEST.py
 




 
 

    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_300_cTau_3.merged/W*   | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_300_cTau_3.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_300_cTau_10.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_300_cTau_10.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_300_cTau_30.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_300_cTau_30.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_500_cTau_10.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_500_cTau_10.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_500_cTau_20.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_500_cTau_20.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_650_cTau_10.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_650_cTau_10.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_650_cTau_20.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_650_cTau_20.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_800_cTau_20.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_800_cTau_20.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_800_cTau_10.merged/W*  | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_800_cTau_10.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_1000_cTau_10.merged/W* | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_1000_cTau_10.py
    ls -alrth /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/Wino_M_1000_cTau_20.merged/W* | awk '{print $9}' | sed -e 's/\/eos\/cms//g' > samples_petrucciani_MG_M_1000_cTau_20.py

    /store/cmst3/user/gpetrucc/SusyWithDeDx/
    
    /eos/cms/store/cmst3/user/gpetrucc/SusyWithDeDx/
    
    Wino_M_300_cTau_3.merged
    Wino_M_300_cTau_10.merged
    Wino_M_300_cTau_30.merged
    Wino_M_500_cTau_10.merged
    Wino_M_500_cTau_20.merged
    Wino_M_650_cTau_10.merged
    Wino_M_650_cTau_20.merged
    Wino_M_800_cTau_20.merged
    Wino_M_800_cTau_10.merged
    Wino_M_1000_cTau_10.merged
    Wino_M_1000_cTau_20.merged
    

    
    cmsRun gendumper_cfg.py   inputFiles=many::samples_TEST.py  \
                              outputFile=/tmp/amassiro/private_samples_TEST.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_300_cTau_10.py  \
                              outputFile=/tmp/amassiro/private_MG_M_300_cTau_10_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_300_cTau_30.py  \
                              outputFile=/tmp/amassiro/private_MG_M_300_cTau_30_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_500_cTau_10.py  \
                              outputFile=/tmp/amassiro/private_MG_M_500_cTau_10_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_500_cTau_20.py  \
                              outputFile=/tmp/amassiro/private_MG_M_500_cTau_20_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_650_cTau_10.py  \
                              outputFile=/tmp/amassiro/private_MG_M_650_cTau_10_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_650_cTau_20.py  \
                              outputFile=/tmp/amassiro/private_MG_M_650_cTau_20_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_800_cTau_20.py  \
                              outputFile=/tmp/amassiro/private_MG_M_800_cTau_20_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_800_cTau_10.py  \
                              outputFile=/tmp/amassiro/private_MG_M_800_cTau_10_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_1000_cTau_10.py  \
                              outputFile=/tmp/amassiro/private_MG_M_1000_cTau_10_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_petrucciani_MG_M_1000_cTau_20.py  \
                              outputFile=/tmp/amassiro/private_MG_M_1000_cTau_20_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
                              
                              
                              
                              
                              
                              
                             
New:
                             
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_300GeV1cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_300GeV1cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_500GeV1cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_500GeV1cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_900GeV1cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_900GeV1cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_900GeV30cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_900GeV30cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_300GeV10cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_300GeV10cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_900GeV10cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_900GeV10cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_500GeV30cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_500GeV30cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
    cmsRun gendumper_cfg.py   inputFiles=many::samples_Py_300GeV30cm_2017.py  \
                              outputFile=/tmp/amassiro/private_Py_300GeV30cm_2017.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                             
                             
                              
                              
                              
    cmsRun gendumper_cfg.py   inputFiles=many::samples_500GeV10cm_noFilter.py  \
                              outputFile=/tmp/amassiro/private_Py_500GeV10cm_2017_nomet.root  \
                              isMiniAod=True  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    
    /eos/cms/store/group/phys_susy/xtracks/noFilter
    
      chargino500GeV_ctau10cm_GEN-SIM_2.root
      chargino500GeV_ctau10cm_GEN-SIM_1.root
      chargino400GeV_ctau1cm_GEN-SIM_1.root
      chargino700GeV_ctau10cm_GEN-SIM_1.root
      chargino800GeV_ctau10cm_GEN-SIM_1.root
      chargino300GeV_ctau10cm_GEN-SIM_1.root
      chargino700GeV_ctau1cm_GEN-SIM_2.root
      chargino600GeV_ctau10cm_GEN-SIM_1.root
      chargino300GeV_ctau1cm_GEN-SIM_1.root
      chargino300GeV_ctau30cm_GEN-SIM_1.root
      chargino500GeV_ctau1cm_GEN-SIM_1.root
      chargino700GeV_ctau30cm_GEN-SIM_1.root

      chargino900GeV_ctau10cm_GEN-SIM_1.root
      chargino500GeV_ctau30cm_GEN-SIM_1.root
      chargino500GeV_ctau1cm_GEN-SIM_1.root
      chargino300GeV_ctau10cm_GEN-SIM_1.root
      chargino900GeV_ctau30cm_GEN-SIM_1.root
      chargino500GeV_ctau10cm_GEN-SIM_1.root
      chargino900GeV_ctau1cm_GEN-SIM_1.root
      chargino300GeV_ctau30cm_GEN-SIM_1.root
      chargino300GeV_ctau1cm_GEN-SIM_1.root



    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino500GeV_ctau10cm_GEN-SIM_2.root  \
                              outputFile=/tmp/amassiro/private_chargino500GeV_ctau10cm_GEN-SIM_2_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino500GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino500GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino400GeV_ctau1cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino400GeV_ctau1cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino700GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino700GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino800GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino800GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino300GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino300GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino600GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino600GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino300GeV_ctau1cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino300GeV_ctau1cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 


    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino300GeV_ctau30cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino300GeV_ctau30cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino500GeV_ctau1cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino500GeV_ctau1cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino700GeV_ctau30cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino700GeV_ctau30cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
                              
                              
New:


    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino900GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino900GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino500GeV_ctau30cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino500GeV_ctau30cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino500GeV_ctau1cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino500GeV_ctau1cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino300GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino300GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino900GeV_ctau30cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino900GeV_ctau30cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino500GeV_ctau10cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino500GeV_ctau10cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino900GeV_ctau1cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino900GeV_ctau1cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino300GeV_ctau30cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino300GeV_ctau30cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

    cmsRun gendumper_cfg.py   inputFiles=file:/eos/cms/store/group/phys_susy/xtracks/noFilter/chargino300GeV_ctau1cm_GEN-SIM_1.root  \
                              outputFile=/tmp/amassiro/private_chargino300GeV_ctau1cm_GEN-SIM_1_nomet.root  \
                              isMiniAod=False  \
                              doLHE=False \
                              mcLHERunInfoTag="" 

                              
                              
                              
                              
      
      
Measure gen met cut efficiency

    r99t   /tmp/amassiro/private_MG_M_500_cTau_10_nomet.root       \
           /tmp/amassiro/private_Py_500GeV10cm_2017_nomet.root           \
           /tmp/amassiro/private_Py_500GeV1cm_2017.root           \
           DrawCompareMET.cxx\(\"genMetTrue\",160,0,2000,\"1\",0,1.0,1.0,1.0\) 
          
    
    From the ratio plot: 0.13114376

    r99t   /tmp/amassiro/private_MG_M_500_cTau_10_nomet.root       \
           /tmp/amassiro/private_Py_500GeV10cm_2017_nomet.root           \
           /tmp/amassiro/private_Py_500GeV1cm_2017.root           \
           DrawCompareMET.cxx\(\"genMetTrue\",160,0,2000,\"1\",0,1.0,1.0,0.13114376\) 
    





    
    
    
    
    r99t   /tmp/amassiro/private_MG_M_300_cTau_10_nomet.root       \
           /tmp/amassiro/private_chargino300GeV_ctau10cm_GEN-SIM_1_nomet.root           \
           /tmp/amassiro/private_Py_300GeV1cm_2017.root           \
           DrawCompareMET.cxx\(\"genMetTrue\",160,0,2000,\"1\",0,1.0,1.0,1.0\) 
          
    1./11.0845 = 0.090216067


    r99t   /tmp/amassiro/private_MG_M_300_cTau_10_nomet.root       \
           /tmp/amassiro/private_chargino300GeV_ctau10cm_GEN-SIM_1_nomet.root           \
           /tmp/amassiro/private_Py_300GeV1cm_2017.root           \
           DrawCompareMET.cxx\(\"genMetTrue\",160,0,2000,\"1\",0,1.0,1.0,0.090216067\) 




    r99t   \
           /tmp/amassiro/private_Py_300GeV1cm_2017.root           \
           /tmp/amassiro/private_Py_500GeV1cm_2017.root           \
           /tmp/amassiro/private_Py_900GeV1cm_2017.root           \
           /tmp/amassiro/private_Py_300GeV30cm_2017.root           \
           /tmp/amassiro/private_Py_900GeV30cm_2017.root           \
           DrawCompareMany.cxx\(\"genMetTrue\",160,0,2000,\"1\",0\) 








    
    
    