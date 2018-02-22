library(gWidgets2)
library(ggplot2)
library(cairoDevice)
library(gWidgetsRGtk2)

path = '/home/niclas.thomas/Desktop/interactiveExamples/data/'
data = read.csv(paste(path,'tips_data.csv',sep=''), header=TRUE)

options(guiToolkit="RGtk2")
win <- gwindow("Interactive Demo")
group <- ggroup(horizontal = FALSE, container = win)

gd <- ggraphics(container=group, width=600, height=600)
d <- dev.cur()

obj <- gbutton("plot", container = group,
               handler = function(h, ...){
                 g <- ggplot(data, aes(x=total_bill, y=tip)) +
                   geom_point(size=5) +
                   labs(x='Total Bill (£)', y='Tip (£)')
                 print(g)
               })

obj <- gbutton("by gender", container = group,
               handler = function(h, ...){
                 g <- ggplot(data, aes(x=total_bill, y=tip)) +
                   geom_point(aes(color=sex), size=5) +
                   labs(x='Total Bill (£)', y='Tip (£)')
                 print(g)
               })

obj <- gbutton("by smoker", container = group,
               handler = function(h, ...){
                 g <- ggplot(data, aes(x=total_bill, y=tip)) +
                   geom_point(aes(color=smoker), size=5) +
                   labs(x='Total Bill (£)', y='Tip (£)')
                 print(g)
               })
