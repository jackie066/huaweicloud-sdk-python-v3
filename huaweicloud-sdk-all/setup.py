# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

from os import path

from setuptools import setup, find_packages

NAME = "huaweicloudsdkall"
VERSION = "3.0.101"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.101',
    'huaweicloudsdkantiddos==3.0.101',
    'huaweicloudsdkaom==3.0.101',
    'huaweicloudsdkapig==3.0.101',
    'huaweicloudsdkapm==3.0.101',
    'huaweicloudsdkas==3.0.101',
    'huaweicloudsdkbcs==3.0.101',
    'huaweicloudsdkbms==3.0.101',
    'huaweicloudsdkbss==3.0.101',
    'huaweicloudsdkbssintl==3.0.101',
    'huaweicloudsdkcampusgo==3.0.101',
    'huaweicloudsdkcbh==3.0.101',
    'huaweicloudsdkcbr==3.0.101',
    'huaweicloudsdkcbs==3.0.101',
    'huaweicloudsdkcc==3.0.101',
    'huaweicloudsdkcce==3.0.101',
    'huaweicloudsdkccm==3.0.101',
    'huaweicloudsdkcdm==3.0.101',
    'huaweicloudsdkcdn==3.0.101',
    'huaweicloudsdkces==3.0.101',
    'huaweicloudsdkcgs==3.0.101',
    'huaweicloudsdkclassroom==3.0.101',
    'huaweicloudsdkcloudbuild==3.0.101',
    'huaweicloudsdkclouddeploy==3.0.101',
    'huaweicloudsdkcloudide==3.0.101',
    'huaweicloudsdkcloudpipeline==3.0.101',
    'huaweicloudsdkcloudrtc==3.0.101',
    'huaweicloudsdkcloudtable==3.0.101',
    'huaweicloudsdkcloudtest==3.0.101',
    'huaweicloudsdkcodecheck==3.0.101',
    'huaweicloudsdkcodecraft==3.0.101',
    'huaweicloudsdkcodehub==3.0.101',
    'huaweicloudsdkcpts==3.0.101',
    'huaweicloudsdkcse==3.0.101',
    'huaweicloudsdkcsms==3.0.101',
    'huaweicloudsdkcss==3.0.101',
    'huaweicloudsdkcts==3.0.101',
    'huaweicloudsdkdas==3.0.101',
    'huaweicloudsdkdbss==3.0.101',
    'huaweicloudsdkdcs==3.0.101',
    'huaweicloudsdkddm==3.0.101',
    'huaweicloudsdkdds==3.0.101',
    'huaweicloudsdkdeh==3.0.101',
    'huaweicloudsdkdevstar==3.0.101',
    'huaweicloudsdkdgc==3.0.101',
    'huaweicloudsdkdli==3.0.101',
    'huaweicloudsdkdms==3.0.101',
    'huaweicloudsdkdns==3.0.101',
    'huaweicloudsdkdrs==3.0.101',
    'huaweicloudsdkdsc==3.0.101',
    'huaweicloudsdkdws==3.0.101',
    'huaweicloudsdkecs==3.0.101',
    'huaweicloudsdkeip==3.0.101',
    'huaweicloudsdkelb==3.0.101',
    'huaweicloudsdkeps==3.0.101',
    'huaweicloudsdkevs==3.0.101',
    'huaweicloudsdkfrs==3.0.101',
    'huaweicloudsdkfunctiongraph==3.0.101',
    'huaweicloudsdkgaussdb==3.0.101',
    'huaweicloudsdkgaussdbfornosql==3.0.101',
    'huaweicloudsdkgaussdbforopengauss==3.0.101',
    'huaweicloudsdkges==3.0.101',
    'huaweicloudsdkgsl==3.0.101',
    'huaweicloudsdkhilens==3.0.101',
    'huaweicloudsdkhss==3.0.101',
    'huaweicloudsdkiam==3.0.101',
    'huaweicloudsdkiec==3.0.101',
    'huaweicloudsdkief==3.0.101',
    'huaweicloudsdkies==3.0.101',
    'huaweicloudsdkimage==3.0.101',
    'huaweicloudsdkimagesearch==3.0.101',
    'huaweicloudsdkims==3.0.101',
    'huaweicloudsdkiotanalytics==3.0.101',
    'huaweicloudsdkiotda==3.0.101',
    'huaweicloudsdkiotedge==3.0.101',
    'huaweicloudsdkivs==3.0.101',
    'huaweicloudsdkkafka==3.0.101',
    'huaweicloudsdkkms==3.0.101',
    'huaweicloudsdkkps==3.0.101',
    'huaweicloudsdklive==3.0.101',
    'huaweicloudsdklts==3.0.101',
    'huaweicloudsdkmeeting==3.0.101',
    'huaweicloudsdkmoderation==3.0.101',
    'huaweicloudsdkmpc==3.0.101',
    'huaweicloudsdkmrs==3.0.101',
    'huaweicloudsdknat==3.0.101',
    'huaweicloudsdknlp==3.0.101',
    'huaweicloudsdkocr==3.0.101',
    'huaweicloudsdkoms==3.0.101',
    'huaweicloudsdkosm==3.0.101',
    'huaweicloudsdkprojectman==3.0.101',
    'huaweicloudsdkrabbitmq==3.0.101',
    'huaweicloudsdkrds==3.0.101',
    'huaweicloudsdkres==3.0.101',
    'huaweicloudsdkrms==3.0.101',
    'huaweicloudsdkrocketmq==3.0.101',
    'huaweicloudsdkroma==3.0.101',
    'huaweicloudsdksa==3.0.101',
    'huaweicloudsdkscm==3.0.101',
    'huaweicloudsdksdrs==3.0.101',
    'huaweicloudsdkservicestage==3.0.101',
    'huaweicloudsdksfsturbo==3.0.101',
    'huaweicloudsdksis==3.0.101',
    'huaweicloudsdksmn==3.0.101',
    'huaweicloudsdksms==3.0.101',
    'huaweicloudsdkswr==3.0.101',
    'huaweicloudsdktms==3.0.101',
    'huaweicloudsdkugo==3.0.101',
    'huaweicloudsdkvas==3.0.101',
    'huaweicloudsdkvcm==3.0.101',
    'huaweicloudsdkvod==3.0.101',
    'huaweicloudsdkvpc==3.0.101',
    'huaweicloudsdkvpcep==3.0.101',
    'huaweicloudsdkvss==3.0.101',
    'huaweicloudsdkwaf==3.0.101',
]

OPTIONS = {
    'bdist_wheel': {
        'universal': True
    }
}

setup(
    name=NAME,
    version=VERSION,
    options=OPTIONS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["huaweicloud", "sdk", "all"],
    packages=find_packages(),
    platforms=['any'],
    install_requires=INSTALL_REQUIRES,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development'
    ]
)
