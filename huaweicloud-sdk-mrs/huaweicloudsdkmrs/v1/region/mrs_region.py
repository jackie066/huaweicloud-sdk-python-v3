# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class MrsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("MRS")


    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://mrs.cn-north-1.myhuaweicloud.cn")

    CN_NORTH_2 = Region(id="cn-north-2", endpoint="https://mrs.cn-north-2.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://mrs.cn-north-4.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://mrs.cn-south-1.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://mrs.cn-east-2.myhuaweicloud.cn")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://mrs.cn-east-3.myhuaweicloud.com")

    AP_SOUTHEAST_1 = Region(id="ap-southeast-1", endpoint="https://mrs.ap-southeast-1.myhuaweicloud.cn")

    AP_SOUTHEAST_2 = Region(id="ap-southeast-2", endpoint="https://mrs.ap-southeast-2.myhuaweicloud.com")

    AP_SOUTHEAST_3 = Region(id="ap-southeast-3", endpoint="https://mrs.ap-southeast-3.myhuaweicloud.com")

    AF_SOUTH_1 = Region(id="af-south-1", endpoint="https://mrs.af-south-1.myhuaweicloud.com")

    RU_NORTHWEST_2 = Region(id="ru-northwest-2", endpoint="https://mrs.ru-northwest-2.myhuaweicloud.cn")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-2": CN_NORTH_2,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "af-south-1": AF_SOUTH_1,
        "ru-northwest-2": RU_NORTHWEST_2,
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


