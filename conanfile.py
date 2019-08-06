from conans import ConanFile
class PlogConan(ConanFile):
    name = "plog"
    version = "1.1.4"
    # No settings/options are necessary, this is header only
    no_copy_source = True

    def source(self):
        self.run("git clone https://github.com/SergiusTheBest/plog.git")
        self.run("cd plog && git checkout tags/" + self.version)

    def package(self):
        self.copy("*.h", src="plog/include", dst="include/plog")   #xxx: changes here

    def package_id(self):
        self.info.header_only()
