class SubsystemBase:
    """
    All subsystems should subclass this.
    Implements periodic input/output and updating the Smart Dashboard.
    """

    def write_periodic_outputs(self):
        """
        Directly interact with hardware using inputs from periodic input/output
        """
        pass

    def read_periodic_inputs(self):
        """
        Set values and readings in periodic input/output from this method
        """
        pass

    def update_on_dashboard(self):
        """
        Put values for this subsystem on the Smart Dashboard
        """
        pass
