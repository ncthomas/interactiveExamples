library(shiny)
library(ggplot2)

path = '/home/niclas.thomas/Desktop/interactiveExamples/data/'
data = read.csv(paste(path,'tips_data.csv',sep=''), header=TRUE)
data = data[,c("smoker","sex","tip","total_bill")]

ui <- fluidPage(
  fluidRow(
    column(width = 4,
           plotOutput("plot1",
                      height = 300,
                      width=800,
                      click = "plot1_click",
                      brush = brushOpts(id = "plot1_brush")
                      )
           )
  ),
  fluidRow(
    column(width = 6,
           h4("Further Information"),
           verbatimTextOutput("click_info"))
    ))

server <- function(input, output) {
  output$plot1 <- renderPlot({
    ggplot(data, aes(x=total_bill, y=tip)) +
      geom_point(aes(color=sex), size=5)
  })
  
  output$click_info <- renderPrint({
    nearPoints(data, input$plot1_click, threshold=100, maxpoints=1, addDist = FALSE)
  })
}

shinyApp(ui, server)



