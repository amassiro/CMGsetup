Effect of HEM on 2018 data
====


Recommendation for HEM:

    https://twiki.cern.ch/twiki/bin/view/CMS/SUSRecommendationsRun2Legacy
    https://hypernews.cern.ch/HyperNews/CMS/get/JetMET/2000.html

This is the "recipe" from jetemet.

From the thread:

In the mean time, we suggest analysts to check the possible impact of
the undercalibration of this region in the following way.
In MC, scale down the jet energy by
    20 % for jets with -1.57 <phi< -0.87 and -2.5<eta<-1.3
    35 % for jets with -1.57 <phi< -0.87 and -3.0<eta<-2.5
(all jets with pt>15 GeV passing the tight ID -in order to reject
muons/electrons-, and propagate this to the MET as well)
Then check the change with respect to the nominal calibration.
If the impact of this scaling on your final result is small, we suggest
to take no action but treat this difference as a systematic uncertainty.





Execute
====

Where:

    /home/amassiro/Cern/Code/CMG/CMGsetup/HEM2018
    
Copy one file to test in local:

    scp amassiro@lxplus.cern.ch:/eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-SIG-SR-2018-Hadded/Wino_M_650_cTau_20/treeProducerXtracks/*.root data/

    scp amassiro@lxplus.cern.ch:/eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-SIG-SR-2018-Hadded/*/treeProducerXtracks/tree.root   data/

    mkdir  Wino_M_300_cTau_3
    mkdir  Wino_M_1000_cTau_20
    mkdir  Wino_M_800_cTau_10
    mkdir  Wino_M_650_cTau_10
    mkdir  Wino_M_300_cTau_30
    mkdir  Wino_M_500_cTau_10
    mkdir  Wino_M_650_cTau_20
    mkdir  Wino_M_1000_cTau_10
    mkdir  Wino_M_500_cTau_20
    mkdir  Wino_M_800_cTau_20
    mkdir  Wino_M_300_cTau_10



    
Run:

    python scaleJet.py data/tree.root data_scaled/tree.root

    ls data/ | grep Wino | awk '{print "python scaleJet.py data/"$1"/tree.root data_scaled/"$1"/tree.root"}'
 
Copy back:

    ls data/ | grep Wino | awk '{print "scp data_scaled/"$1"/tree.root amassiro@lxplus.cern.ch:/eos/cms/store/group/phys_exotica/xtracks/7Sep2019/Calibrated-SIG-SR-2018-Hadded/"$1"/treeProducerXtracks/tree_hem.root "}'

    
    

Test:

    r99t  data_scaled/tree.root
    
    tree->Draw("Jet_pt_hem / Jet_pt")
    
    tree->Draw("met_pt_hem / met_pt")

    

    tree->SetLineColor(kBlue)
    tree->Draw("met_pt")
    tree->SetLineColor(kRed)
    tree->Draw("met_pt_hem", "", "same")
