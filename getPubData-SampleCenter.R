# Change the treehousePubSamples data into just their data house



treehousePubSamples 
# load data from the file from treehouse website and call it treehousePubSamples

# like this
# treehousePubSamples<-lapply('input_file', function(x) {
# 		read_tsv(x, col_types=cols()) %>%
# 		})  %>%
# 		bind_rows()






# Rename a column in R
colnames(treehousePubSamples)[colnames(treehousePubSamples)=="[0-9]"] <- ""


lapply(treehousePubSamples, function(y) as.numeric(gsub("(.)", "/^(.*?)_/", y)))


treehousePubSamples2 <- gsub(treehousePubSamples %>% colnames(),"(.)","/^(.*?)_/")

treehousePubSamplesTest 


treehouseTest <- treehousePubSamples
for (col in treehouseTest %>% colnames()){
	colnames(treehouseTest)[colnames(treehouseTest)==col] <- gsub('([_].*)',"",col)

	colnames(treehouseTest)[colnames(treehouseTest)==col] <- gsub('([-].*)',"",col)
}
