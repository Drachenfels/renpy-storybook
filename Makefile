CACHE_EXT=*.rpyc *.rpyb

clean:
	@for i in $(CACHE_EXT); do find . -name "$$i" -delete; done
