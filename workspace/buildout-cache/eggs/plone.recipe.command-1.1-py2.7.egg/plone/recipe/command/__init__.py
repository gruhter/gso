from subprocess import call
import logging
import zc.buildout

class Recipe:
    def __init__(self, buildout, name, options):
        self.options = options
        self.logger = logging.getLogger(name)

        stop_on_error = self.options.get('stop-on-error')
        if stop_on_error is None or stop_on_error.lower() in ('no', 'off', 'false'):
            self.stop_on_error = False
        elif stop_on_error.lower() in ('yes', 'on', 'true'):
            self.stop_on_error = True
        else:
            msg = "Invalid value '%s' for 'stop_on_error', use 'yes', 'on', 'true', 'no', 'off' or false." % stop_on_error
            self.logger.error(msg)
            raise zc.buildout.UserError(msg)

    def _execute(self, command):
        retcode = call(command, shell=True)
        if self.stop_on_error and retcode != 0:
            msg = "Non zero exit code (%s) while running command." % retcode
            self.logger.error(msg)
            raise zc.buildout.UserError(msg)

    def install(self):
        command = self.options.get('command', None)
        if not command:
            msg="No command specified"
            self.logger.error(msg)
            raise zc.buildout.UserError(msg)

        self.logger.info("Running '%s'" % command)
        self._execute(command)
        location = self.options.get('location')
        if location is not None:
            return location.split()
        else:
            return ()

    def update(self):
        command = self.options.get('update-command')
        if command is not None:
            self.logger.info("Running %s" % command)
            self._execute(command)
