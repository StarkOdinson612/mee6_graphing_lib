import matplotlib.pyplot as plt
import datetime
import json


class Plotter:
    def __init__(self):
        self.time_format_str = "%d-%B-%Y %H:%M:%S"

    def plotter_1(self):

        with open("db.json", "r") as fo:
            db = json.loads(fo.read())

        keys = list(db.keys())[0:100]

        c = []

        for z in range(10):
            for r in range(10):
                index_to_get = z * 10 + r

                c += [index_to_get]

                e = keys[index_to_get]

                dates = [
                    (datetime.datetime.strptime(i, self.time_format_str)).strftime(
                        "%-d-%b-%-y"
                    )
                    for i in db[e]["xp_data"].keys()
                ]
                # dates = [i for i in db[e]['xp_data'].keys()]
                plt.plot(dates, db[e]["xp_data"].values(), label=db[e]["name"])

            plt.grid()
            plt.xlabel("Dates")
            plt.xticks(rotation=-45, ha="left")
            plt.ylabel("XP")
            plt.title(f"XP Data {r + 1}")
            plt.legend(loc="best", bbox_to_anchor=(1, 1))
            # plt.show()
            # plt.figure(figsize=(8,8));
            plt.savefig(f"static/plot{z + 1}.png", bbox_inches="tight", dpi=200)
            plt.close()
