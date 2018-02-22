library(ggplot2)
library(plotly)

path = '/home/niclas.thomas/Desktop/interactiveExamples/data/'
data = read.csv(paste(path,'tips_data.csv',sep=''), header=TRUE)

## Example 1
g = ggplot( data, aes(x=total_bill, y=tip)) +
  geom_point() +
  labs(x='Total Bill (£)', y='Tip (£)') +
  theme_bw()
g

## Example 2
g = ggplot( data, aes(x=total_bill, y=tip)) +
  geom_point() +
  geom_smooth(method='lm') +
  labs(x='Total Bill (£)', y='Tip (£)') +
  theme_bw()
g

## Example 3
p <- plot_ly(data = data, type='scatter',
             x = ~total_bill,
             y = ~tip,
             color=~sex,
             mode='markers',
             text=~smoker,
             colors=c('blue','green'),
             marker = list(size = 10))
p
