# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ApplicationGatewaySkuName(str, Enum):

    standard_small = "Standard_Small"
    standard_medium = "Standard_Medium"
    standard_large = "Standard_Large"


class ApplicationGatewayTier(str, Enum):

    standard = "Standard"


class IPAllocationMethod(str, Enum):

    static = "Static"
    dynamic = "Dynamic"


class TransportProtocol(str, Enum):

    udp = "Udp"
    tcp = "Tcp"


class SecurityRuleProtocol(str, Enum):

    tcp = "Tcp"
    udp = "Udp"
    asterisk = "*"


class SecurityRuleAccess(str, Enum):

    allow = "Allow"
    deny = "Deny"


class SecurityRuleDirection(str, Enum):

    inbound = "Inbound"
    outbound = "Outbound"


class RouteNextHopType(str, Enum):

    virtual_network_gateway = "VirtualNetworkGateway"
    vnet_local = "VnetLocal"
    internet = "Internet"
    virtual_appliance = "VirtualAppliance"
    none = "None"


class ApplicationGatewayProtocol(str, Enum):

    http = "Http"
    https = "Https"


class ApplicationGatewayCookieBasedAffinity(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ApplicationGatewayRequestRoutingRuleType(str, Enum):

    basic = "Basic"
    path_based_routing = "PathBasedRouting"


class ApplicationGatewayOperationalState(str, Enum):

    stopped = "Stopped"
    starting = "Starting"
    running = "Running"
    stopping = "Stopping"


class AuthorizationUseStatus(str, Enum):

    available = "Available"
    in_use = "InUse"


class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(str, Enum):

    not_configured = "NotConfigured"
    configuring = "Configuring"
    configured = "Configured"
    validation_needed = "ValidationNeeded"


class ExpressRouteCircuitPeeringType(str, Enum):

    azure_public_peering = "AzurePublicPeering"
    azure_private_peering = "AzurePrivatePeering"
    microsoft_peering = "MicrosoftPeering"


class ExpressRouteCircuitPeeringState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class ExpressRouteCircuitSkuTier(str, Enum):

    standard = "Standard"
    premium = "Premium"


class ExpressRouteCircuitSkuFamily(str, Enum):

    unlimited_data = "UnlimitedData"
    metered_data = "MeteredData"


class ServiceProviderProvisioningState(str, Enum):

    not_provisioned = "NotProvisioned"
    provisioning = "Provisioning"
    provisioned = "Provisioned"
    deprovisioning = "Deprovisioning"


class LoadDistribution(str, Enum):

    default = "Default"
    source_ip = "SourceIP"
    source_ip_protocol = "SourceIPProtocol"


class ProbeProtocol(str, Enum):

    http = "Http"
    tcp = "Tcp"


class NetworkOperationStatus(str, Enum):

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"


class VirtualNetworkGatewayType(str, Enum):

    vpn = "Vpn"
    express_route = "ExpressRoute"


class VpnType(str, Enum):

    policy_based = "PolicyBased"
    route_based = "RouteBased"


class VirtualNetworkGatewaySkuName(str, Enum):

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"


class VirtualNetworkGatewaySkuTier(str, Enum):

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"


class ProcessorArchitecture(str, Enum):

    amd64 = "Amd64"
    x86 = "X86"


class VirtualNetworkGatewayConnectionType(str, Enum):

    ipsec = "IPsec"
    vnet2_vnet = "Vnet2Vnet"
    express_route = "ExpressRoute"
    vpn_client = "VPNClient"


class VirtualNetworkGatewayConnectionStatus(str, Enum):

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"