# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class DdmRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("DDM")


    CN_SOUTHWEST_2 = Region(id="cn-southwest-2", endpoint="https://ddm.cn-southwest-2.myhuaweicloud.com")

    CN_SOUTH_2 = Region(id="cn-south-2", endpoint="https://ddm.cn-south-2.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://ddm.cn-north-4.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://ddm.cn-east-3.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://ddm.cn-east-2.myhuaweicloud.com")

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://ddm.cn-north-1.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://ddm.cn-south-1.myhuaweicloud.com")

    AP_SOUTHEAST_1 = Region(id="ap-southeast-1", endpoint="https://ddm.ap-southeast-1.myhuaweicloud.com")

    LA_NORTH_2 = Region(id="la-north-2", endpoint="https://ddm.la-north-2.myhuaweicloud.com")

    SA_BRAZIL_1 = Region(id="sa-brazil-1", endpoint="https://ddm.sa-brazil-1.myhuaweicloud.com")

    LA_SOUTH_2 = Region(id="la-south-2", endpoint="https://ddm.la-south-2.myhuaweicloud.com")

    static_fields = {
        "cn-southwest-2": CN_SOUTHWEST_2,
        "cn-south-2": CN_SOUTH_2,
        "cn-north-4": CN_NORTH_4,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
        "cn-north-1": CN_NORTH_1,
        "cn-south-1": CN_SOUTH_1,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "la-north-2": LA_NORTH_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-south-2": LA_SOUTH_2,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id.")

        fields = static_fields if static_fields else cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("Unexpected region_id: " + region_id)


