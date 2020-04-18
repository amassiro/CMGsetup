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













































    
    
    