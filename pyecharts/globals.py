# coding=utf-8

BUILTIN_THEMES = ["light", "dark", "white"]
ONLINE_HOST = "http://chenjiandongx.com/go-echarts-assets/assets/"


class _RenderType:
    CANVAS: str = "canvas"
    SVG: str = "svg"


class _FileType:
    SVG: str = "svg"
    PNG: str = "png"
    JPEG: str = "jpeg"
    HTML: str = "html"


class _SymbolType:
    RECT: str = "rect"
    ROUND_RECT: str = "roundRect"
    TRIANGLE: str = "triangle"
    DIAMOND: str = "diamond"
    ARROW: str = "arrow"


class _ChartType:
    BAR: str = "bar"
    BOXPLOT: str = "boxplot"
    EFFECT_SCATTER: str = "effectScatter"
    FUNNEL: str = "funnel"
    GAUGE: str = "gauge"
    GEO: str = "geo"
    GRAPH: str = "graph"
    HEATMAP: str = "heatmap"
    KLINE: str = "candlestick"
    LINE: str = "line"
    LINES: str = "lines"
    LIQUID: str = "liquidFill"
    MAP: str = "map"
    PARALLEL: str = "parallel"
    PIE: str = "pie"
    POLAR: str = "polar"
    RADAR: str = "radar"
    SANKEY: str = "sankey"
    SCATTER: str = "scatter"
    THEMERIVER: str = "themeRiver"
    TREE: str = "tree"
    TREEMAP: str = "treemap"
    WORDCLOUD: str = "wordCloud"


class _ToolTipFormatterType:
    GEO = """function (params) {
        return params.name + ' : ' + params.value[2];
    }"""
    GAUGE = "{a} <br/>{b} : {c}%"


class _ThemeType:
    LIGHT = "light"
    DARK = "dark"
    CHALK: str = "chalk"
    ESSOS: str = "essos"
    INFOGRAPHIC: str = "infographic"
    MACARONS: str = "macarons"
    PURPLE_PASSION: str = "purple-passion"
    ROMA: str = "roma"
    ROMANTIC: str = "romantic"
    SHINE: str = "shine"
    VINTAGE: str = "vintage"
    WALDEN: str = "walden"
    WESTEROS: str = "westeros"
    WONDERLAND: str = "wonderland"


class _GeoType:
    SCATTER: str = "scatter"
    EFFECT_SCATTER: str = "effectScatter"
    HEATMAP: str = "heatmap"
    LINES: str = "lines"


RenderType = _RenderType()
FileType = _FileType()
SymbolType = _SymbolType()
ChartType = _ChartType
TooltipFormatterType = _ToolTipFormatterType()
ThemeType = _ThemeType()
GeoType = _GeoType()
