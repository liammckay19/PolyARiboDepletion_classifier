# R code for grabbing a few columns from big dataset


options(stringsAsFactors=FALSE) # for compatibile code between us

library(tidyverse)


liamsWorkingDir <-
  "~/Documents/UCSC/Junior/BME 160/PolyARiboDepletion_classifier"

setwd(paste0(liamsWorkingDir))

file=list.files(, "treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv")

treehousePubSamples<-lapply(file, function(x) {
  read_tsv(x, col_types=cols())
}) 	%>%
  bind_rows()

