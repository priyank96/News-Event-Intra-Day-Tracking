from bokeh.charts import output_file, Line, save
from selenium import webdriver
from EntityClass import EntityClass
plots = dict()

def prepare_plots(entities):
    for i in entities:
        plots[i.id] = webdriver.Chrome()


def plot(lines, id):
    #print(lines)
    output_file(id+".html",title=id)
    p = Line(lines,plot_width=1000,plot_height=800)
    save(p)
    plots[id].get("file:///C:/Users/Prism/Desktop/Priyank/csp5/"+id+".html")
    #plots[id].navigate().to("file:///C:/Users/Prism/Desktop/Priyank/csp5/"+id+".html")



if __name__=='__main__':
    from closest_lines import get_lines_hl
    lines = get_lines_hl()
    prepare_plots([EntityClass('Sample')])
    plot(lines,'Sample')
    plot(lines, 'Sample')
