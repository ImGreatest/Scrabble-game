import platform


class SystemManager:
    def __init__(self):
        # detail description os
        self._platform = platform.platform()
        # name release os
        self._release = platform.release()
        # version os
        self._version = platform.version()
        # information architecture os
        self._architecture = platform.architecture()

    def __getattribute__(self, item):
        return super.__getattribute__(item)

    def __str__(self):
        return f'{self._platform}, {self._release}, {self._version}, {self._architecture}'

    def __repr__(self):
        return (
            f'System information: platform - {self._platform}, release - {self._release}, version - {self._version}, '
            f'architecture - {self._architecture}')

    @property
    def platform(self):
        return self._platform

    @platform.getter
    def platform(self):
        return self._platform

    @property
    def release(self):
        return self._release

    @release.getter
    def release(self):
        return self._release

    @property
    def version(self):
        return self._version

    @version.getter
    def version(self):
        return self._version

    @property
    def architecture(self):
        return self._architecture

    @architecture.getter
    def architecture(self):
        return self._architecture
