PROTO_DIR = src
PROTO_FILES = $(wildcard $(PROTO_DIR)/*.proto)

PROTO_GEN_DIR = build
PROTO_GEN_CPP_DIR = $(PROTO_GEN_DIR)/cpp
PROTO_GEN_CSHARP_DIR = $(PROTO_GEN_DIR)/csharp
PROTO_GEN_JAVA_DIR = $(PROTO_GEN_DIR)/java
PROTO_GEN_JS_DIR = $(PROTO_GEN_DIR)/js
PROTO_GEN_KOTLIN_DIR = $(PROTO_GEN_DIR)/kotlin
PROTO_GEN_OBJC_DIR = $(PROTO_GEN_DIR)/objc
PROTO_GEN_PHP_DIR = $(PROTO_GEN_DIR)/php
PROTO_GEN_PYTHON_DIR = $(PROTO_GEN_DIR)/python
PROTO_GEN_RUBY_DIR = $(PROTO_GEN_DIR)/ruby

INCLUDES_DEPENDENCY = /usr/local/include

DOC_PLUGIN = protoc-gen-doc=/usr/bin/protoc-gen-doc
DOC_DIR = docs
DOC_OPT = html,index.html

gen:
	mkdir -p $(PROTO_GEN_CPP_DIR) $(PROTO_GEN_CSHARP_DIR) \
		$(PROTO_GEN_JAVA_DIR) $(PROTO_GEN_JS_DIR) \
		$(PROTO_GEN_KOTLIN_DIR) $(PROTO_GEN_OBJC_DIR) \
		$(PROTO_GEN_PHP_DIR) $(PROTO_GEN_PYTHON_DIR) \
		$(PROTO_GEN_RUBY_DIR)

	mkdir -p $(DOC_DIR)

	protoc -I$(INCLUDES_DEPENDENCY) -I=$(PROTO_DIR) $(PROTO_FILES) \
		--plugin=$(DOC_PLUGIN) --doc_out=$(DOC_DIR) --doc_opt=$(DOC_OPT) \
		--cpp_out=$(PROTO_GEN_CPP_DIR) \
		--csharp_out=$(PROTO_GEN_CSHARP_DIR) \
		--java_out=$(PROTO_GEN_JAVA_DIR) \
		--js_out=$(PROTO_GEN_JS_DIR) \
		--kotlin_out=$(PROTO_GEN_KOTLIN_DIR) \
		--objc_out=$(PROTO_GEN_OBJC_DIR) \
		--php_out=$(PROTO_GEN_PHP_DIR) \
		--python_out=$(PROTO_GEN_PYTHON_DIR) \
		--ruby_out=$(PROTO_GEN_RUBY_DIR)

clean:
	rm -rf $(PROTO_GEN_DIR)

.PHONY: gen clean
