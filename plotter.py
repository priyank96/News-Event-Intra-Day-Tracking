from bokeh.plotting import output_file, save, figure
from selenium import webdriver

plots = dict()

def prepare_plots(entities):
    done = []
    for i in entities:
        if i.id not in done:
            plots[i.id] = webdriver.Firefox()
        done.append(i.id)

def plot(lines, id):
    #print(lines)
    output_file(id+".html",title=id)
    p = figure(plot_width=600,plot_height=600)
    p.line(x=list(range(0,len(lines[0]))),y=lines[0])
    save(p)
    #plots[id].get("file:///home/priyank/Documents/News-Event-Intra-Day-Tracking-master/"+id+".html")
    #plots[id].navigate().to("file:///C:/Users/Prism/Desktop/Priyank/csp5/"+id+".html")




