normalize <- function(){
  for(i in 1:150){
    iris$Sepal.Length[i] <- (iris$Sepal.Length[i]-Min_SL)/(Max_SL-Min_SL)
    iris$Sepal.Width[i] <- (iris$Sepal.Width[i]-Min_SW)/(Max_SW-Min_SW)
    iris$Petal.Length[i] <- (iris$Petal.Length[i]-Min_PL)/(Max_PL-Min_PL)
    iris$Petal.Width[i] <- (iris$Petal.Width[i]-Min_PW)/(Max_PW-Min_PW)
  }
}


New_Columns<-function(){
  for(i in 1:150){
    Species <- iris$Species[i]
    if(i==0) print(Species)
    iris$Setosa[i] <- 0
    iris$Virginica[i]<-0
    iris$Versicolor[i]<-0
    if(Species == "virginica") iris$Virginica[i] <-1
    if(Species == "versicolor") iris$Versicolor[i] <-1
    if(Species == "vetosa") iris$Setosa[i]<-1
  }
}