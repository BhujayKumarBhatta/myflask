import ms2app

from ms2app.APIroutes.firstapi import bp1

bp_list = [bp1]

app = ms2app.create_app(blue_print_list=bp_list)