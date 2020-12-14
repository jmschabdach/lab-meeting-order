path <- "~/lab-meeting-order" # sets location of .txt name file

namelist <- read.delim(paste(path,"names.txt",sep = '/'),header = F) # reads txt file

sample(namelist[,1],replace = F) # prints random names