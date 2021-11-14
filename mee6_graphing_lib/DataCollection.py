import asyncio
import time
import json
import datetime
import mee6_graphing_lib.Plotter
import mee6_graphing_lib.API_Fetch_Class


class DataCollection:
    def get_details(self):
        _api = new API_Fetch_Class()
        _plot = new Plotter()

        details = []

        xp_trigger = False

        with open("db.json", "r") as fo:
            db = json.load(fo)

        for i in range(100):
            tom = asyncio.run(_api.API_fetch(i))

            if xp_trigger:
                break

            for l in tom["players"]:
                if l["xp"] < 300:
                    xp_trigger = True
                    break

                try:
                    asd = db[l["id"]]
                    temp_xp_data = asd["xp_data"]
                    temp_xp_data.update(
                        {time.strftime(time_format_str, time.gmtime()): l["xp"]}
                    )

                    # print(temp_xp_data)

                    db.update(
                        {l["id"]: {"name": l["username"], "xp_data": temp_xp_data}}
                    )

                    # print(db[l["id"]])

                except:
                    db.update(
                        {
                            l["id"]: {
                                "name": l["username"],
                                "xp_data": {
                                    time.strftime(time_format_str, time.gmtime()): l[
                                        "xp"
                                    ]
                                },
                            }
                        }
                    )

                details += [{int(l["id"]): l["xp"]}]

            # print(i)

        with open("db.json", "w+") as fo:
            json.dump(db, fo, indent=2)

        plotter_1()

        # print(details)

        # pl/otter_1(db)
        # for i in range(1, 864001):
        #     print(i)
        #     time.sleep(1)

        return
