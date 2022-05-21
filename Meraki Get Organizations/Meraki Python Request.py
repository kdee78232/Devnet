#Meraki Python Request  Get Organizations
#Operation Id:getOrganizations 
#Description:List the organizations that the user has privileges on




import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))








#output below

 [
    {
        "id": "681155",
        "name": "DeLab",
        "url": "https://n392.meraki.com/o/49Gm_c/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "per-device" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "573083052582915028",
        "name": "NexttttttttttLab",
        "url": "https://n18.meraki.com/o/PoiDucs/manage/organization/overview",
        "api": { "enabled": false },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583819",
        "name": "My changed org",
        "url": "https://n22.meraki.com/o/TDt5Jcw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583708",
        "name": "hello",
        "url": "https://n22.meraki.com/o/hC66edw/manage/organization/overview",
        "api": { "enabled": false },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583536",
        "name": "TNF - The Network Factory",
        "url": "https://n22.meraki.com/o/K5Faybw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "573083052582914605",
        "name": "Jacks_test_net",
        "url": "https://n18.meraki.com/o/22Uqhas/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "549236",
        "name": "DevNet Sandbox",
        "url": "https://n149.meraki.com/o/-t35Mb/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "per-device" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583264",
        "name": "My organization",
        "url": "https://n22.meraki.com/o/aLMnNaw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583237",
        "name": "Xirg",
        "url": "https://n22.meraki.com/o/ZF92zcw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583213",
        "name": "sample_network",
        "url": "https://n22.meraki.com/o/IJQKjbw/manage/organization/overview",
        "api": { "enabled": false },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "573083052582914233",
        "name": "organization with name changed",
        "url": "https://n18.meraki.com/o/TY6awbs/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583197",
        "name": "The New Org",
        "url": "https://n22.meraki.com/o/wXe-Faw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583158",
        "name": "Testlab",
        "url": "https://n22.meraki.com/o/AvGDGdw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583134",
        "name": "Wotan",
        "url": "https://n22.meraki.com/o/U3paXbw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583133",
        "name": "MuthanaAPITest",
        "url": "https://n22.meraki.com/o/NBowlcw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583131",
        "name": "thienbao",
        "url": "https://n22.meraki.com/o/dADP-cw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583128",
        "name": "trungheo",
        "url": "https://n22.meraki.com/o/XjvDBcw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583093",
        "name": "The Org",
        "url": "https://n22.meraki.com/o/yotmJcw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583071",
        "name": "PM_Test",
        "url": "https://n22.meraki.com/o/lUmuUdw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583051",
        "name": "trung",
        "url": "https://n22.meraki.com/o/4lFkacw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396583031",
        "name": "My organization",
        "url": "https://n22.meraki.com/o/N1e3qdw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396582986",
        "name": "DevNet Test Org",
        "url": "https://n22.meraki.com/o/yZVJIcw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396582973",
        "name": "DevNet Test Org",
        "url": "https://n22.meraki.com/o/4ApTKbw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396582756",
        "name": "Personal.Lekhnath",
        "url": "https://n22.meraki.com/o/HjSXiaw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396582755",
        "name": "Your Organization",
        "url": "https://n22.meraki.com/o/LwDcydw/manage/organization/overview",
        "api": { "enabled": false },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396582738",
        "name": "My organization",
        "url": "https://n22.meraki.com/o/wzbgjbw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396582684",
        "name": "SVR",
        "url": "https://n22.meraki.com/o/rMNradw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "566327653141842188",
        "name": "DevNetAssoc",
        "url": "https://n6.meraki.com/o/dcGsWag/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "575334852396582591",
        "name": "Ftreqah organization",
        "url": "https://n22.meraki.com/o/Kpj8kdw/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "52636",
        "name": "Forest City - Other",
        "url": "https://n42.meraki.com/o/E_utnd/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "865776",
        "name": "Cisco Live US 2019",
        "url": "https://n22.meraki.com/o/CVQqTb/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    },
    {
        "id": "463308",
        "name": "dev ",
        "url": "https://n18.meraki.com/o/vB2D8a/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "per-device" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        }
    }
]
