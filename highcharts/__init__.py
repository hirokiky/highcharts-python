import encoders
import options
from common import *
from config_sections import *


class Chart(DictBacked):
    '''
    The base config for a highcharts chart.

    See http://www.highcharts.com/ref/ for available options.
    '''
    available_options = options.CHART
    defaults = {
        "series": [],
        "chart": ChartConfig,
        "credits": CreditsConfig,
        "title": TitleConfig,
        "subtitle": SubtitleConfig,
        "legend": LegendConfig,
        "tooltip": TooltipConfig,
        "xAxis": XAxisConfig,
        "yAxis": YAxisConfig
    }

    def add_series(self, series):
        self.series.append(series)

    def to_json(self, cls=encoders.ObjectEncoder):
        return encoders.dump_json(self, cls=cls)

    def __str__(self):
        return self.to_json()
