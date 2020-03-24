Production of private sample
====




  # SIM-DIGI step with PU premixing

        cmsDriver.py \
        --datatier GEN-SIM-RAW \
        --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW
" \
        --conditions 94X_mc2017_realistic_v14 \
        --mc \
        --eventcontent PREMIXRAW \
        --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT \
        --nThreads 8 \
        --datamix PreMix \
        --era Run2_2017 \
        --filein file:$input_path/chargino${mass}GeV_ctau${length}cm_GEN-SIM_${iJob}.root \
        --fileout file:chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW_${iJob}.root \
        --python_filename scripts/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW_${iJob}.py \
        --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizePr
oduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
        --customise_commands 'process.PREMIXRAWEventContent.outputCommands.extend(["keep *_trackingParticleRecoTrackAsssociation
_*_*", "keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*"])' \
        -n -1751 \
        —no_exec



   # RECO step

      cmsDriver.py \
      --step RAW2DIGI,RECO,RECOSIM,EI \
      --mc \
      --datatier RECO \
      --conditions 94X_mc2017_realistic_v14 \
      --eventcontent AODSIM \
      --era Run2_2017 \
      --nThreads 8 \
      --runUnscheduled  \
      --filein file:$input_path/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW_${iJob}.root \
      --fileout file:chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW-RECO_${iJob}.root \
      --python_filename scripts/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW-RECO_${iJob}.py \
      --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProd
uce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
      --customise_commands 'process.AODSIMEventContent.outputCommands.extend(["keep *_siPixelClusters_*_*", "keep *_siStripClust
ers_*_*", "keep *_dedxHitInfo_*_*", "keep recoTrackExtras_generalTracks_*_*", "keep TrackingRecHitsOwned_generalTracks_*_*", "ke
ep *_trackingParticleRecoTrackAsssociation_*_*"])' \
      -n -1 \
      --no_exec

# MINIAOD step

      cmsDriver.py miniAOD \
      --step PAT \
      --datatier MINIAODSIM \
      --conditions 94X_mc2017_realistic_v14 \
      --eventcontent MINIAODSIM \
      --era Run2_2017 \
      --mc \
      --filein file:$input_path/chargino${mass}GeV_ctau${length}cm_GEN-SIM-RAW-RECO_${iJob}.root \
      --fileout file:chargino${mass}GeV_ctau${length}cm_miniAOD_${iJob}.root \
      --python_filename scripts/chargino${mass}GeV_ctau${length}cm_miniAOD_${iJob}.py \
      --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProd
uce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep \
      --customise_commands 'process.MINIAODSIMEventContent.outputCommands.extend(["keep *_dedxHitInfo_*_*", "keep recoTrackExtra
s_generalTracks_*_*", "keep *_isolatedTracks_*_*", "keep recoGenParticles_prunedGenParticles_*_*"])' \
      -n -1 \
      --no_exec \
      --runUnscheduled

      
      
      