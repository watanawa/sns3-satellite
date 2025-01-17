/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2013 Magister Solutions Ltd
 * Copyright (c) 2018 CNES
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Author: Sami Rantanen <sami.rantanen@magister.fi>
 * Author: Mathias Ettinger <mettinger@viveris.toulouse.fr>
 */

#ifndef SATELLITE_GW_HELPER_H
#define SATELLITE_GW_HELPER_H

#include <string>

#include <ns3/object-factory.h>
#include <ns3/net-device-container.h>
#include <ns3/node-container.h>
#include <ns3/traced-callback.h>

#include <ns3/satellite-channel.h>
#include <ns3/satellite-ncc.h>
#include <ns3/satellite-link-results.h>
#include <ns3/satellite-mac.h>
#include <ns3/satellite-bbframe-conf.h>
#include <ns3/satellite-superframe-sequence.h>
#include <ns3/satellite-typedefs.h>

namespace ns3 {

/**
 * \brief Creates needed objects for GW nodes like SatGeoNetDevice objects.
 *        Handles needed configuration for the GW nodes.
 *
 */
class SatGwHelper : public Object
{
public:
  /**
   * Random access setting options.
   */
  typedef struct
  {
    SatEnums::RandomAccessModel_t m_randomAccessModel;
    SatPhyRxCarrierConf::InterferenceModel m_raInterferenceModel;
    SatPhyRxCarrierConf::InterferenceEliminationModel m_raInterferenceEliminationModel;
    SatPhyRxCarrierConf::RandomAccessCollisionModel m_raCollisionModel;
    double m_raConstantErrorRate;
  } RandomAccessSettings_s;

  /**
   * \brief Get the type ID
   * \return the object TypeId
   */
  static TypeId GetTypeId (void);
  TypeId GetInstanceTypeId (void) const;

  /**
   * Default constructor.
   */
  SatGwHelper ();
  /**
   * Create a SatGwHelper to make life easier when creating Satellite point to
   * point network connections.
   */
  SatGwHelper (SatTypedefs::CarrierBandwidthConverter_t carrierBandwidthConverter,
               uint32_t fwdLinkCarrierCount,
               Ptr<SatSuperframeSeq> seq,
               SatMac::ReadCtrlMsgCallback readCb,
               SatMac::ReserveCtrlMsgCallback reserveCb,
               SatMac::SendCtrlMsgCallback sendCb,
               RandomAccessSettings_s randomAccessSettings);

  virtual ~SatGwHelper ()
  {
  }

  /*
   * Initializes the GW helper based on attributes
   * \param lrRcs2 return link results
   * \param lrFwd DVB-S2 or DVB-S2X link results
   * \param dvbVersion The DVB version chosen
   */
  void Initialize (Ptr<SatLinkResultsRtn> lrRcs2, Ptr<SatLinkResultsFwd> lrFwd, SatEnums::DvbVersion_t dvbVersion);

  /**
   * Get BB frame configuration.
   *
   * \return BB frame configuration create by helper.
   */
  Ptr<SatBbFrameConf> GetBbFrameConf () const;

  /**
   * Set an attribute value to be propagated to each NetDevice created by the
   * helper.
   *
   * \param name the name of the attribute to set
   * \param value the value of the attribute to set
   *
   * Set these attributes on each ns3::SatNetDevice created
   * by SatGwHelper::Install
   */
  void SetDeviceAttribute (std::string name, const AttributeValue &value);

  /**
   * Set an attribute value to be propagated to each Channel created by the
   * helper.
   *
   * \param name the name of the attribute to set
   * \param value the value of the attribute to set
   *
   * Set these attribute on each ns3::SatChannel created
   * by SatGwHelper::Install
   */
  void SetChannelAttribute (std::string name, const AttributeValue &value);

  /**
   * Set an attribute value to be propagated to each Phy created by the helper.
   *
   * \param name the name of the attribute to set
   * \param value the value of the attribute to set
   *
   * Set these attributes on each ns3::SatNetDevice created
   * by SatGwHelper::Install
   */
  void SetPhyAttribute (std::string name, const AttributeValue &value);

  /**
   * \param c a set of nodes
   * \param gwId  id of the gw
   * \param beamId  id of the beam
   * \param fCh forward channel
   * \param rCh return channel
   * \param ncc NCC (Network Control Center)
   *
   * This method creates a ns3::SatChannel with the
   * attributes configured by SatGwHelper::SetChannelAttribute,
   * then, for each node in the input container, we create a
   * ns3::SatNetDevice with the requested attributes,
   * a queue for this ns3::SatNetDevice, and associate the resulting
   * ns3::SatNetDevice with the ns3::Node and ns3::SatChannel.
   */
  NetDeviceContainer InstallDvb (NodeContainer c,
                                 uint32_t gwId,
                                 uint32_t beamId,
                                 Ptr<SatChannel> fCh,
                                 Ptr<SatChannel> rCh,
                                 Ptr<SatNcc> ncc,
                                 Ptr<SatLowerLayerServiceConf> llsConf);

  /**
   * \param n node
   * \param gwId  id of the gw
   * \param beamId  id of the beam
   * \param fCh forward channel
   * \param rCh return channel
   * \param ncc NCC (Network Control Center)
   *
   * Saves you from having to construct a temporary NodeContainer.
   */
  Ptr<NetDevice> InstallDvb (Ptr<Node> n,
                             uint32_t gwId,
                             uint32_t beamId,
                             Ptr<SatChannel> fCh,
                             Ptr<SatChannel> rCh,
                             Ptr<SatNcc> ncc,
                             Ptr<SatLowerLayerServiceConf> llsConf);

  /**
   * \param c a set of nodes
   * \param gwId  id of the gw
   * \param beamId  id of the beam
   * \param fCh forward channel
   * \param rCh return channel
   * \param ncc NCC (Network Control Center)
   *
   * This method creates a ns3::SatChannel with the
   * attributes configured by SatGwHelper::SetChannelAttribute,
   * then, for each node in the input container, we create a
   * ns3::SatLorawanNetDevice with the requested attributes,
   * a queue for this ns3::SatLorawanNetDevice, and associate the resulting
   * ns3::SatLorawanNetDevice with the ns3::Node and ns3::SatChannel.
   */
  NetDeviceContainer InstallLora (NodeContainer c,
                                  uint32_t gwId,
                                  uint32_t beamId,
                                  Ptr<SatChannel> fCh,
                                  Ptr<SatChannel> rCh,
                                  Ptr<SatNcc> ncc,
                                  Ptr<SatLowerLayerServiceConf> llsConf);

  /**
   * \param n node
   * \param gwId  id of the gw
   * \param beamId  id of the beam
   * \param fCh forward channel
   * \param rCh return channel
   * \param ncc NCC (Network Control Center)
   *
   * Saves you from having to construct a temporary NodeContainer.
   */
  Ptr<NetDevice> InstallLora (Ptr<Node> n,
                              uint32_t gwId,
                              uint32_t beamId,
                              Ptr<SatChannel> fCh,
                              Ptr<SatChannel> rCh,
                              Ptr<SatNcc> ncc,
                              Ptr<SatLowerLayerServiceConf> llsConf);

  /**
   * Enables creation traces to be written in given file
   * \param stream  stream for creation trace outputs
   * \param cb  callback to connect traces
   */
  void EnableCreationTraces (Ptr<OutputStreamWrapper> stream, CallbackBase &cb);

private:
  SatTypedefs::CarrierBandwidthConverter_t m_carrierBandwidthConverter;
  uint32_t m_rtnLinkCarrierCount;
  Ptr<SatSuperframeSeq> m_superframeSeq;

  Ptr<SatBbFrameConf> m_bbFrameConf;

  // The control message container callbacks
  SatMac::ReadCtrlMsgCallback     m_readCtrlCb;
  SatMac::ReserveCtrlMsgCallback  m_reserveCtrlCb;
  SatMac::SendCtrlMsgCallback     m_sendCtrlCb;

  ObjectFactory m_channelFactory;
  ObjectFactory m_deviceFactory;

  /*
   * Configured dedicated access interference model for the return link. Set as an attribute.
   */
  SatPhy::InterferenceModel m_daInterferenceModel;

  /*
   * Configured error model for the return link. Set as an attribute.
   */
  SatPhy::ErrorModel m_errorModel;

  /*
   * Constant error rate for dedicated access in the RTN link.
   */
  double m_daConstantErrorRate;

  /*
   * Return channel link results (DVB-RCS2) are created if ErrorModel
   * is configured to be AVI. Note, that only one instance of the
   * link results is needed for all GWs.
   */
  Ptr<SatLinkResults> m_linkResults;

  /**
   * \brief Trace callback for creation traces
   */
  TracedCallback<std::string> m_creationTrace;

  double m_symbolRate;

  /**
   * Enable channel estimation error modeling at forward link
   * receiver (= UT).
   */
  bool m_enableChannelEstimationError;

  /**
   * \brief The used random access model settings
   */
  RandomAccessSettings_s m_raSettings;

  /**
   * \brief The forward link algorithm used
   */
  SatEnums::FwdSchedulingAlgorithm_t m_fwdSchedulingAlgorithm;
};

} // namespace ns3

#endif /* SATELLITE_GW_HELPER_H */
