library(shiny)

path = '/home/niclas.thomas/Desktop/interactiveExamples/data/'
data = read.csv(paste(path,'box_data.csv',sep=''), header=TRUE)

ui <- fluidPage(
  tags$head(tags$style(HTML("
                    pre, table.table {
                    font-size: smaller;
                    }
                    "))
    ),
  fluidRow(
    column(width = 4,
           plotOutput("plot1",
                      height = 350,
                      width=600,
                      click = "plot_click",
                      hover = hoverOpts(id = "plot_hover", delay=50)
                      )
           )
    ),
  fluidRow(
    column(width = 3,
           verbatimTextOutput("click_info")
    ),
    column(width = 3,
           verbatimTextOutput("hover_info")
    )
  )
    )


server <- function(input, output) {
  
  RV <- reactiveValues(x_clicks=c(), y_clicks=c(), x_hover=c(), y_hover=c())
  
  output$plot1 <- renderPlot({
      plot(c(-1, 10), c(-1, 10), type= "n", xlab = "", ylab = "")
      rect(data$xmin, data$ymin, data$xmax, data$ymax, col = "orange", border = "black")
      if (!is.null(RV$x_hover)){
        input$plot_hover
        isolate({
          lines(RV$x_hover, RV$y_hover, type='l', xlim=c(-1,10), ylim=c(-1,10))
          })
      }
  })
  
  observeEvent(input$plot_click, {
    click <- input$plot_click
    RV$x_clicks <- c(RV$x_clicks,click$x)
    RV$y_clicks <- c(RV$y_clicks,click$y)
  })
  
  observeEvent(input$plot_hover, {
    hover <- input$plot_hover
    RV$x_hover <- c(RV$x_hover,hover$x)
    RV$y_hover <- c(RV$y_hover,hover$y)
  })
}

shinyApp(ui, server)

