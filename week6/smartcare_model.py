"""SmartCare v0.3 - domain class skeletons.

Traced to the v0.2 requirements. Behaviour is not implemented yet;
each method records the requirement it will have to satisfy.
"""

# FR-07: status is one value from a fixed list.
BOOKED = "Booked"
COMPLETED = "Completed"
CANCELLED = "Cancelled"
VALID_STATUSES = (BOOKED, COMPLETED, CANCELLED)


class Patient:
    """One person the clinic treats. FR-01 to FR-03."""

    def __init__(self, patient_id, given_name, family_name, date_of_birth):
        self.patient_id = patient_id        # FR-01, never reused (NFR-05)
        self.given_name = given_name
        self.family_name = family_name
        self.date_of_birth = date_of_birth

    def update_details(self, given_name, family_name, date_of_birth):
        """FR-03. patient_id is deliberately not a parameter."""
        pass

    def full_name(self):
        """FR-02 and AC-01."""
        pass


class Practitioner:
    """Someone who sees patients. FR-04."""

    def __init__(self, practitioner_id, name, role):
        self.practitioner_id = practitioner_id
        self.name = name
        self.role = role

    def display_name(self):
        """AC-01, for the booking confirmation."""
        pass


class Appointment:
    """One patient with one practitioner at one date and time. FR-05."""

    def __init__(self, appointment_id, patient, practitioner,
                 date, start_time):
        self.appointment_id = appointment_id
        self.patient = patient              # FR-05: exactly one
        self.practitioner = practitioner    # FR-05: exactly one
        self.date = date
        self.start_time = start_time
        self.status = BOOKED                # new appointments start Booked

    def change_status(self, new_status):
        """FR-08. Must refuse anything outside VALID_STATUSES."""
        pass

    def cancel(self):
        """FR-09. Sets status only - never deletes (NFR-05)."""
        pass

    def is_booked(self):
        """Helper for FR-06 and FR-11."""
        pass

    def clashes_with(self, practitioner, date, start_time):
        """FR-06. True only if this one is Booked and all three match."""
        pass

    def move_to(self, date, start_time):
        """FR-12. Called only after the book confirms there is no clash."""
        pass


class AppointmentBook:
    """Owns every appointment and enforces the clash rule.

    FR-06, FR-10, FR-11, FR-12. Kept free of any print() or input()
    so the rules can be tested without the interface (NFR-03, NFR-04).
    """

    def __init__(self):
        self.appointments = []   # cancelled ones stay in here (NFR-05)

    def book(self, patient, practitioner, date, start_time):
        """FR-05 and FR-06. Returns the new Appointment, or refuses."""
        pass

    def reschedule(self, appointment, date, start_time):
        """FR-12. Re-checks, then asks the appointment to move itself."""
        pass

    def cancel(self, appointment):
        """FR-09."""
        pass

    def for_patient(self, patient):
        """FR-10. Date order, cancelled ones included."""
        pass

    def for_practitioner_on(self, practitioner, date):
        """FR-11. Cancelled ones excluded."""
        pass

    def _has_clash(self, practitioner, date, start_time):
        """FR-06. The one rule no single Appointment can check alone."""
        pass

    # Note: there is deliberately no remove() or delete() anywhere
    # in this file. NFR-05 says nothing is permanently deleted, so
    # the safest way to enforce that is to give the code no way to.
