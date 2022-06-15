import cherrypy
import json
import requests
import time
import datetime
import pandas as pd

class GridSplitServer(object):

    exposed = True
    def GET(self,*uri,**params):

        if len(uri) != 0:

            # load dataset of 15-01-2021
            filepath = '2021_01_15_tot_grid_split.csv'
            df = pd.read_csv(filepath)
            df['datetime'] = pd.to_datetime(df['datetime'])
            df.set_index('datetime', inplace=True)

            # EMISSION FACTORS [CO2e g/kWh]
            path = 'emission_factors.json'
            f = open(path)
            emission_factors = json.load(f)

            # CURRENT DATE
            currDate = datetime.datetime.now()
            dt = pd.to_datetime(currDate)
            #dt_time = dt.time
            dt = pd.to_datetime('2021-01-15 ' + str(dt.hour) + ':' + str(dt.minute) + ':' + str(dt.second))
            s = df.iloc[df.index.get_loc(dt, method='nearest')]
            #s = df.iloc[df['time'].get_loc(dt_time, method='nearest')]

            # GET METHOD RESPONSE
            if uri[0] == 'consumption':
                response = {}
                response['value'] = s['electricity_consumption']
                return json.dumps(response)

            elif uri[0] == 'cumulative_consumption':
                response = {}
                response['value'] = df.iloc[:df.index.get_loc(dt, method='nearest')]['electricity_consumption'].values.sum()
                return json.dumps(response)

            elif uri[0] == 'emissions':
                CO2 = 0
                CO2 += s['%_wind'] * emission_factors['wind']
                CO2 += s['%_hydro'] * emission_factors['hydro']
                CO2 += s['%_nuclear'] * emission_factors['nuclear']
                CO2 += s['%_thermal'] * emission_factors['thermal']
                CO2 += s['%_other'] * emission_factors['other']
                CO2 += s['%_solar'] * emission_factors['solar']
                response = {}
                response['value'] = CO2
                return json.dumps(response)

            elif uri[0] == 'cumulative_emissions':
                response = {}
                wind = df.iloc[:df.index.get_loc(dt, method='nearest')]['%_wind'].values.sum()
                hydro = df.iloc[:df.index.get_loc(dt, method='nearest')]['%_hydro'].values.sum()
                nuclear = df.iloc[:df.index.get_loc(dt, method='nearest')]['%_nuclear'].values.sum()
                thermal = df.iloc[:df.index.get_loc(dt, method='nearest')]['%_thermal'].values.sum()
                other = df.iloc[:df.index.get_loc(dt, method='nearest')]['%_other'].values.sum()
                solar = df.iloc[:df.index.get_loc(dt, method='nearest')]['%_solar'].values.sum()

                CO2 = 0
                CO2 += wind * emission_factors['wind']
                CO2 += hydro * emission_factors['hydro']
                CO2 += nuclear * emission_factors['nuclear']
                CO2 += thermal * emission_factors['thermal']
                CO2 += other * emission_factors['other']
                CO2 += solar * emission_factors['solar']

                response = {}
                response['value'] = CO2
                return json.dumps(response)

            elif uri[0] == 'wind':
                response = {}
                response['value'] = s['%_wind']
                return json.dumps(response)

            elif uri[0] == 'hydro':
                response = {}
                response['value'] = s['%_hydro']
                return json.dumps(response)

            elif uri[0] == 'nuclear':
                response = {}
                response['value'] = s['%_nuclear']
                return json.dumps(response)

            elif uri[0] == 'thermal':
                response = {}
                response['value'] = s['%_thermal']
                return json.dumps(response)

            elif uri[0] == 'other':
                response = {}
                response['value'] = s['%_other']
                return json.dumps(response)

            elif uri[0] == 'solar':
                response = {}
                response['value'] = s['%_solar']
                return json.dumps(response)

            elif uri[0] == 'all':
                response = {}
                response['value'] = s.tolist()[:-1]
                return json.dumps(response)


if __name__ == '__main__':
    
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }
    cherrypy.tree.mount(GridSplitServer(), '/', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 50000})
    cherrypy.engine.start()
    cherrypy.engine.block()