# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class DrsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("DRS")


    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://drs.cn-north-4.myhuaweicloud.com")

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://drs.cn-north-1.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://drs.cn-south-1.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://drs.cn-east-3.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://drs.cn-east-2.myhuaweicloud.com")

    CN_NORTH_2 = Region(id="cn-north-2", endpoint="https://drs.cn-north-2.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
        "cn-north-2": CN_NORTH_2,
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


