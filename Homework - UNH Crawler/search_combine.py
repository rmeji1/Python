import searcher
import indexer

d = indexer.process_data("raw_data.pickle", "fortune_shelves");
searcher.search("fortune_shelves");
