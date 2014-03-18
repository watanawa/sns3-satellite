# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('satellite', ['internet', 'propagation', 'antenna', 'csma', 'stats', 'flow-monitor'])
    module.source = [
        'model/cbr-application.cc',
        'model/geo-coordinate.cc',
        'model/ideal-net-device.cc',
        'model/satellite-antenna-gain-pattern.cc',
        'model/satellite-antenna-gain-pattern-container.cc',
        'model/satellite-arp-cache.cc',
        'model/satellite-base-encapsulator.cc',
        'model/satellite-base-fader.cc',
        'model/satellite-base-fader-conf.cc',
        'model/satellite-base-fading.cc',
        'model/satellite-base-trace-container.cc',        
        'model/satellite-bbframe.cc',
        'model/satellite-bbframe-container.cc',        
        'model/satellite-beam-scheduler.cc',
        'model/satellite-channel.cc',
        'model/satellite-channel-estimation-error.cc',
        'model/satellite-channel-estimation-error-container.cc',
        'model/satellite-cno-estimator.cc',
        'model/satellite-composite-sinr-output-trace-container.cc',
        'model/satellite-constant-interference.cc',
        'model/satellite-constant-position-mobility-model.cc',
        'model/satellite-control-message.cc',
        'model/satellite-crdsa-replica-tag.cc',
        'model/satellite-dama-entry.cc',
        'model/satellite-encap-pdu-status-tag.cc',
        'model/satellite-fading-external-input-trace.cc',
        'model/satellite-fading-external-input-trace-container.cc',
        'model/satellite-fading-input-trace.cc',
        'model/satellite-fading-input-trace-container.cc',
        'model/satellite-fading-output-trace-container.cc',
        'model/satellite-fading-oscillator.cc',
        'model/satellite-fwd-link-scheduler.cc',
        'model/satellite-frame-allocator.cc',
        'model/satellite-free-space-loss.cc',
        'model/satellite-generic-stream-encapsulator.cc',
        'model/satellite-geo-feeder-phy.cc',
        'model/satellite-geo-net-device.cc',
        'model/satellite-geo-user-phy.cc',
        'model/satellite-gse-headers.cc',
        'model/satellite-gw-llc.cc',  
        'model/satellite-gw-mac.cc',   
        'model/satellite-gw-phy.cc',
        'model/satellite-id-mapper.cc',
        'model/satellite-interference.cc',
        'model/satellite-interference-input-trace-container.cc',        
        'model/satellite-interference-output-trace-container.cc',
        'model/satellite-link-results.cc',
        'model/satellite-llc.cc',           
        'model/satellite-loo-conf.cc',
        'model/satellite-loo-model.cc',
        'model/satellite-look-up-table.cc',
        'model/satellite-lower-layer-service.cc',
        'model/satellite-mac.cc',
        'model/satellite-mac-tag.cc',       
        'model/satellite-markov-conf.cc',
        'model/satellite-markov-container.cc',
        'model/satellite-markov-model.cc',
        'model/satellite-mobility-model.cc',
        'model/satellite-mobility-observer.cc',        
        'model/satellite-ncc.cc',
        'model/satellite-net-device.cc',
        'model/satellite-node-info.cc',
        'model/satellite-packet-trace.cc',
        'model/satellite-per-packet-interference.cc',
        'model/satellite-phy.cc',
        'model/satellite-phy-rx.cc',
        'model/satellite-phy-rx-carrier.cc',
        'model/satellite-phy-rx-carrier-conf.cc',
        'model/satellite-phy-tx.cc',               
        'model/satellite-position-allocator.cc',
        'model/satellite-propagation-delay-model.cc',
        'model/satellite-queue.cc',
        'model/satellite-random-access-allocation-channel.cc',
        'model/satellite-random-access-container.cc',
        'model/satellite-random-access-container-conf.cc',
        'model/satellite-rayleigh-conf.cc',
        'model/satellite-rayleigh-model.cc',
        'model/satellite-request-manager.cc', 
        'model/satellite-return-link-encapsulator.cc',
        'model/satellite-rle-header.cc',
        'model/satellite-rx-power-input-trace-container.cc',        
        'model/satellite-rx-power-output-trace-container.cc',
        'model/satellite-scheduling-object.cc',
        'model/satellite-signal-parameters.cc',
        'model/satellite-tbtp-container.cc',
        'model/satellite-time-tag.cc',
        'model/satellite-traced-interference.cc',
        'model/satellite-ut-llc.cc',        
        'model/satellite-ut-mac.cc',
        'model/satellite-ut-phy.cc',
        'model/satellite-ut-scheduler.cc',
        'model/virtual-channel.cc',
        'utils/satellite-env-variables.cc',
        'utils/satellite-input-fstream-time-double-container.cc',
        'utils/satellite-input-fstream-time-long-double-container.cc',
        'utils/satellite-input-fstream-wrapper.cc',
        'utils/satellite-output-fstream-double-container.cc',
        'utils/satellite-output-fstream-long-double-container.cc',
        'utils/satellite-output-fstream-string-container.cc',
        'utils/satellite-output-fstream-wrapper.cc',
        'helper/cbr-helper.cc',
        'helper/cbr-kpi-helper.cc',
        'helper/kpi-helper.cc',
        'helper/onoff-kpi-helper.cc',
        'helper/satellite-bbframe-conf.cc',
        'helper/satellite-beam-helper.cc',
        'helper/satellite-beam-user-info.cc',
        'helper/satellite-conf.cc',
        'helper/satellite-frame-conf.cc',
        'helper/satellite-geo-helper.cc',
        'helper/satellite-gw-helper.cc',
        'helper/satellite-helper.cc',
        'helper/satellite-superframe-sequence.cc',
        'helper/satellite-user-helper.cc',
        'helper/satellite-ut-helper.cc',
        'helper/satellite-wave-form-conf.cc',
        'stats/satellite-stats-helper.cc',
        'stats/satellite-stats-fwd-app-delay-helper.cc',
        'stats/satellite-stats-fwd-app-throughput-helper.cc',
        'stats/satellite-stats-fwd-dev-throughput-helper.cc',
        'stats/satellite-stats-rtn-app-delay-helper.cc',
        'stats/satellite-stats-rtn-app-throughput-helper.cc',
        'stats/satellite-stats-helper-container.cc',
        ]

    module_test = bld.create_ns3_module_test_library('satellite')
    module_test.source = [
        'test/cbr-test.cc',
        'test/geo-coordinate-test.cc',
        'test/link-results-test.cc',
        'test/performance-memory-test.cc',
        'test/satellite-antenna-pattern-test.cc',
        'test/satellite-channel-estimation-error-test.cc',
        'test/satellite-control-msg-container-test.cc',
        'test/satellite-cno-estimator-test.cc',
        'test/satellite-fading-trace-test.cc',
        'test/satellite-fsl-test.cc',
        'test/satellite-gse-test.cc',
        'test/satellite-interference-test.cc',
        'test/satellite-mobility-test.cc',
        'test/satellite-mobility-observer-test.cc',
        'test/satellite-rle-test.cc',
        'test/satellite-per-packet-if-test.cc',
        'test/satellite-scenario-creation.cc',
        'test/satellite-simple-unicast.cc',
        'test/satellite-waveform-conf-test.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'satellite'
    headers.source = [
        'model/cbr-application.h',
        'model/geo-coordinate.h',
        'model/ideal-net-device.h',
        'model/satellite-antenna-gain-pattern.h',
        'model/satellite-antenna-gain-pattern-container.h',        
        'model/satellite-arp-cache.h',
        'model/satellite-base-encapsulator.h',
        'model/satellite-base-fader.h',
        'model/satellite-base-fader-conf.h',
        'model/satellite-base-fading.h',
        'model/satellite-base-trace-container.h',        
        'model/satellite-bbframe.h',
        'model/satellite-bbframe-container.h',       
        'model/satellite-beam-scheduler.h',
        'model/satellite-channel.h',
        'model/satellite-channel-estimation-error.h',
        'model/satellite-channel-estimation-error-container.h',
        'model/satellite-cno-estimator.h',
        'model/satellite-composite-sinr-output-trace-container.h',
        'model/satellite-constant-interference.h',
        'model/satellite-constant-position-mobility-model.h',
        'model/satellite-control-message.h',
        'model/satellite-crdsa-replica-tag.h',
        'model/satellite-dama-entry.h',
        'model/satellite-encap-pdu-status-tag.h',
        'model/satellite-enums.h',
        'model/satellite-fading-external-input-trace.h',
        'model/satellite-fading-external-input-trace-container.h',
        'model/satellite-fading-input-trace.h',
        'model/satellite-fading-input-trace-container.h',
        'model/satellite-fading-oscillator.h',
        'model/satellite-fading-output-trace-container.h',
        'model/satellite-frame-allocator.h',
        'model/satellite-free-space-loss.h',
        'model/satellite-fwd-link-scheduler.h',       
        'model/satellite-generic-stream-encapsulator.h',
        'model/satellite-geo-feeder-phy.h',       
        'model/satellite-geo-net-device.h',
        'model/satellite-geo-user-phy.h',
        'model/satellite-gse-headers.h',
        'model/satellite-gw-llc.h',  
        'model/satellite-gw-mac.h',  
        'model/satellite-gw-phy.h',
        'model/satellite-id-mapper.h',
        'model/satellite-interference.h',
        'model/satellite-interference-input-trace-container.h',        
        'model/satellite-interference-output-trace-container.h',        
        'model/satellite-link-results.h',
        'model/satellite-llc.h',      
        'model/satellite-loo-conf.h',
        'model/satellite-loo-model.h',
        'model/satellite-look-up-table.h',
        'model/satellite-lower-layer-service.h',
        'model/satellite-mac.h',
        'model/satellite-mac-tag.h',        
        'model/satellite-markov-conf.h',
        'model/satellite-markov-container.h',
        'model/satellite-markov-model.h',
        'model/satellite-mobility-model.h',
        'model/satellite-mobility-observer.h',
        'model/satellite-ncc.h',
        'model/satellite-net-device.h',
        'model/satellite-node-info.h',
        'model/satellite-packet-trace.h',
        'model/satellite-per-packet-interference.h',
        'model/satellite-phy.h',
        'model/satellite-phy-rx.h',
        'model/satellite-phy-rx-carrier.h',
        'model/satellite-phy-rx-carrier-conf.h',
        'model/satellite-phy-tx.h',               
        'model/satellite-position-allocator.h',
        'model/satellite-propagation-delay-model.h',
        'model/satellite-queue.h',
        'model/satellite-random-access-allocation-channel.h',
        'model/satellite-random-access-container.h',
        'model/satellite-random-access-container-conf.h',
        'model/satellite-rayleigh-conf.h',
        'model/satellite-rayleigh-model.h',
        'model/satellite-request-manager.h',
        'model/satellite-return-link-encapsulator.h',
        'model/satellite-rle-header.h',
        'model/satellite-rx-power-input-trace-container.h',        
        'model/satellite-rx-power-output-trace-container.h',
        'model/satellite-scheduling-object.h',
        'model/satellite-signal-parameters.h',
        'model/satellite-tbtp-container.h',
        'model/satellite-time-tag.h',
        'model/satellite-traced-interference.h',
        'model/satellite-ut-llc.h',        
        'model/satellite-ut-mac.h',
        'model/satellite-ut-phy.h',
        'model/satellite-ut-scheduler.h',
    	'model/satellite-utils.h',
        'model/virtual-channel.h',
        'utils/satellite-env-variables.h',
        'utils/satellite-input-fstream-time-double-container.h',
        'utils/satellite-input-fstream-time-long-double-container.h',
        'utils/satellite-input-fstream-wrapper.h',
        'utils/satellite-output-fstream-double-container.h',
        'utils/satellite-output-fstream-long-double-container.h',
        'utils/satellite-output-fstream-string-container.h',
        'utils/satellite-output-fstream-wrapper.h',
        'helper/cbr-helper.h',
        'helper/cbr-kpi-helper.h',
        'helper/kpi-helper.h',
        'helper/onoff-kpi-helper.h',
        'helper/satellite-bbframe-conf.h',
        'helper/satellite-beam-helper.h',
        'helper/satellite-beam-user-info.h',
        'helper/satellite-conf.h',
        'helper/satellite-frame-conf.h',
        'helper/satellite-geo-helper.h',
        'helper/satellite-gw-helper.h',
        'helper/satellite-helper.h',
        'helper/satellite-superframe-sequence.h',
        'helper/satellite-user-helper.h',
        'helper/satellite-ut-helper.h',
        'helper/satellite-wave-form-conf.h',
        'stats/satellite-stats-helper.h',
        'stats/satellite-stats-fwd-app-delay-helper.h',
        'stats/satellite-stats-fwd-app-throughput-helper.h',
        'stats/satellite-stats-fwd-dev-throughput-helper.h',
        'stats/satellite-stats-rtn-app-delay-helper.h',
        'stats/satellite-stats-rtn-app-throughput-helper.h',
        'stats/satellite-stats-helper-container.h',
        ]

    if (bld.env['ENABLE_EXAMPLES']):
        bld.recurse('examples')

    # bld.ns3_python_bindings()

