from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms.models import User 

import uuid


class Account(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True, null=True, blank=True,db_index=True)
    password_hash = models.TextField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    googleid = models.TextField(unique=True, null=True, blank=True, db_index=True) 
    phone = models.TextField(unique=True, null=True, blank=True, db_index=True) 
    passport_number = models.TextField(unique=True, null=True, blank=True, db_index=True)
    passport_verified = models.BooleanField(default=False)
    national_id_fan = models.TextField(unique=True, null=True, blank=True, db_index=True)
    national_id_fan_verified = models.BooleanField(default=False)

                                

    class Meta:
        db_table = 'Account'


class EmailVerification(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, db_column='accountId',db_index=True)
    token = models.TextField(unique=True,db_index=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'EmailVerification'


class PasswordReset(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, db_column='accountId',db_index=True)
    token = models.TextField(unique=True,db_index=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'PasswordReset'


class User(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4)
    account = models.OneToOneField(Account, on_delete=models.RESTRICT, db_column='accountId',db_index=True)
    first_name = models.TextField(null=True, blank=True, db_index=True)
    last_name = models.TextField(null=True, blank=True, db_index=True)
    avatar_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.TextField(null=True, blank=True, unique=True, db_index=True)
    rating_score = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    total_deliveries_completed = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'User'


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        db_table = 'location'


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True,db_index=True)
    line1 = models.TextField(null=True, blank=True)
    line2 = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True,db_index=True)
    region_code = models.CharField(max_length=2, null=True, blank=True,db_index=True)
    region_name = models.TextField(null=True, blank=True,db_index=True)
    country_code = models.CharField(max_length=2, null=True, blank=True,db_index=True)

    class Meta:
        db_table = 'addresses'
        unique_together = ('id',)


# class BillingAddress(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, db_column='account_id')
#     address_location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'billing_address'


# class GoogleMaps(models.Model):
#     id = models.AutoField(primary_key=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     maps_link = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'google_maps'


# class Airport(models.Model):
#     id = models.AutoField(primary_key=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     airport_code = models.CharField(max_length=3, null=True, blank=True)

#     class Meta:
#         db_table = 'airport'


# class File(models.Model):
#     id = models.AutoField(primary_key=True)
#     file_path = models.CharField(max_length=255, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'files'


# class Image(models.Model):
#     image_id = models.AutoField(primary_key=True)
#     file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'images'


# class LengthConversion(models.Model):
#     id = models.AutoField(primary_key=True)
#     meters = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     feet = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     inches = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     class Meta:
#         db_table = 'length_conversions'


# class WeightConversion(models.Model):
#     id = models.AutoField(primary_key=True)
#     kilograms = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     pounds = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     ounces = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     class Meta:
#         db_table = 'weight_conversions'


# class ItemHeight(models.Model):
#     id = models.AutoField(primary_key=True)
#     length_conversion = models.ForeignKey(LengthConversion, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'item_height'
#         unique_together = ('id',)


# class ItemWidth(models.Model):
#     id = models.AutoField(primary_key=True)
#     length_conversion = models.ForeignKey(LengthConversion, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'item_width'
#         unique_together = ('id',)


# class ItemLength(models.Model):
#     id = models.AutoField(primary_key=True)
#     length_conversion = models.ForeignKey(LengthConversion, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'item_length'
#         unique_together = ('id',)


# class VolumetricWeight(models.Model):
#     volumetric_weight_id = models.AutoField(primary_key=True)
#     item_height = models.ForeignKey(ItemHeight, on_delete=models.SET_NULL, null=True, blank=True)
#     item_width = models.ForeignKey(ItemWidth, on_delete=models.SET_NULL, null=True, blank=True)
#     item_length = models.ForeignKey(ItemLength, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'volumetric_weight'


# class GovernmentId(models.Model):
#     id = models.AutoField(primary_key=True)
#     document_type = models.CharField(max_length=255, null=True, blank=True)
#     image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'government_id'
#         unique_together = ('id',)


# class UserContactInformation(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, db_column='account_id')
#     phone_number = models.TextField(null=True, blank=True)
#     telegram_username = models.TextField(null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)

#     class Meta:
#         db_table = 'user_contact_information'
#         unique_together = ('id',)


# class UserKyc(models.Model):
#     kyc_id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, db_column='account_id')
#     first_name = models.TextField(null=True, blank=True)
#     last_name = models.TextField(null=True, blank=True)
#     residence_address = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     government_id = models.ForeignKey(GovernmentId, on_delete=models.SET_NULL, null=True, blank=True)
#     contact_information = models.ForeignKey(UserContactInformation, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'user_kyc'
#         unique_together = ('kyc_id',)


# class FlightVerification(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_kyc = models.ForeignKey(UserKyc, on_delete=models.SET_NULL, null=True, blank=True)
#     pnr = models.CharField(max_length=6)
#     passenger_name = models.TextField(null=True, blank=True)
#     flight_number = models.TextField(null=True, blank=True)
#     departure_airport = models.CharField(max_length=3, null=True, blank=True)
#     arrival_airport = models.CharField(max_length=3, null=True, blank=True)
#     departure_datetime = models.DateTimeField(null=True, blank=True)
#     arrival_datetime = models.DateTimeField(null=True, blank=True)
#     retrieval_timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'flight_verification'
#         unique_together = ('id',)
#         verbose_name = 'Flight Verification'
#         verbose_name_plural = 'Flight Verifications'


# class Shipment(models.Model):
#     shipment_id = models.AutoField(primary_key=True)
#     sender_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, 
#                                       related_name='sent_shipments', db_column='sender_account_id')
#     payment = models.OneToOneField('Payment', on_delete=models.SET_NULL, null=True, blank=True, 
#                                   db_column='payment_id')
#     created_at = models.DateTimeField(auto_now_add=True)
#     payment_responsibility = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True,
#                                              related_name='responsible_for_payments')

#     class Meta:
#         db_table = 'shipment'


# class Item(models.Model):
#     item_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255, null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     quantity = models.IntegerField(null=True, blank=True)
#     declared_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     item_category = models.CharField(max_length=255, null=True, blank=True)
#     handling_notes = models.TextField(null=True, blank=True)
#     shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, blank=True)
#     possessed_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     item_weight = models.ForeignKey(WeightConversion, on_delete=models.SET_NULL, null=True, blank=True)
#     volumetric_weight = models.ForeignKey(VolumetricWeight, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'item'


# class ItemImage(models.Model):
#     id = models.AutoField(primary_key=True)
#     image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
#     sort_order = models.IntegerField(null=True, blank=True)
#     item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'item_images'


# class Consignee(models.Model):
#     consignee_id = models.AutoField(primary_key=True)
#     shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, blank=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'consignee'


# class CourierRequirements(models.Model):
#     courier_requirements_id = models.AutoField(primary_key=True)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     ready_date = models.DateField(null=True, blank=True)
#     origin_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True,
#                                        related_name='courier_requirements_origin')
#     destination_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True,
#                                            related_name='courier_requirements_destination')
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'courier_requirements'


# class Itinerary(models.Model):
#     itinerary_id = models.AutoField(primary_key=True)
#     courier_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     departure = models.DateTimeField(null=True, blank=True)
#     arrival = models.DateTimeField(null=True, blank=True)
#     available_weight = models.ForeignKey(WeightConversion, on_delete=models.SET_NULL, null=True, blank=True)
#     available_space = models.ForeignKey(VolumetricWeight, on_delete=models.SET_NULL, null=True, blank=True)
#     origin_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True,
#                                       related_name='itinerary_origin')
#     destination_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True,
#                                            related_name='itinerary_destination')
#     created_at = models.DateTimeField(auto_now_add=True)
#     flight_verification = models.ForeignKey(FlightVerification, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'itinerary'


# class ItemProposal(models.Model):
#     item_proposal_id = models.AutoField(primary_key=True)
#     shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, blank=True)
#     itinerary = models.ForeignKey(Itinerary, on_delete=models.SET_NULL, null=True, blank=True)
#     item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'item_proposal'


# class PickupWindowAgreement(models.Model):
#     id = models.AutoField(primary_key=True)
#     pickup_window_start = models.DateField(null=True, blank=True)
#     pickup_window_end = models.DateField(null=True, blank=True)
#     is_final = models.BooleanField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'pickup_window_agreement'
#         unique_together = ('id',)


# class DelveryWindowAgreement(models.Model):
#     id = models.AutoField(primary_key=True)
#     delivery_window_start = models.DateField(null=True, blank=True)
#     delivery_window_end = models.DateField(null=True, blank=True)
#     is_final = models.BooleanField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'delvery_window_agreement'
#         unique_together = ('id',)


# class AgreedCourierHandoverDateTimes(models.Model):
#     id = models.AutoField(primary_key=True)
#     pickup_window_agreement = models.ForeignKey(PickupWindowAgreement, on_delete=models.SET_NULL, null=True, blank=True)
#     agreed_date_time = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'agreed_courier_handover_date_times'
#         unique_together = ('id',)


# class AgreedConsigneeHandoverDateTime(models.Model):
#     id = models.AutoField(primary_key=True)
#     delivery_window_agreement = models.ForeignKey(DelveryWindowAgreement, on_delete=models.SET_NULL, null=True, blank=True)
#     agreed_date_time = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'agreed_consignee_handover_date_time'
#         unique_together = ('id',)


# class LocationAgreement(models.Model):
#     id = models.AutoField(primary_key=True)
#     meetup_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     item_proposal = models.ForeignKey(ItemProposal, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'location_agreement'


# class ShipperCourierLocation(models.Model):
#     id = models.AutoField(primary_key=True)
#     location_agreement = models.ForeignKey(LocationAgreement, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'shipper_courier_location'
#         unique_together = ('id',)


# class ConsigneeCourierLocation(models.Model):
#     id = models.AutoField(primary_key=True)
#     location_agreement = models.ForeignKey(LocationAgreement, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'consignee_courier_location'
#         unique_together = ('id',)


# class PriceAgreement(models.Model):
#     id = models.AutoField(primary_key=True)
#     item_proposal = models.ForeignKey(ItemProposal, on_delete=models.SET_NULL, null=True, blank=True)
#     agreed_price = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'price_agreement'
#         unique_together = ('id',)


# class ShipperHandoverAgreement(models.Model):
#     id = models.AutoField(primary_key=True)
#     shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, blank=True)
#     item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
#     remarks = models.TextField(null=True, blank=True)
#     price_agreement = models.ForeignKey(PriceAgreement, on_delete=models.SET_NULL, null=True, blank=True)
#     date_time_agreement = models.ForeignKey(AgreedCourierHandoverDateTimes, on_delete=models.SET_NULL, null=True, blank=True)
#     shipper_courier_location_agreement = models.ForeignKey(ShipperCourierLocation, on_delete=models.SET_NULL, null=True, blank=True)
#     all_agreements_done = models.BooleanField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'shipper_handover_agreement'


# class CourierHandoverAgreement(models.Model):
#     id = models.AutoField(primary_key=True)
#     shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, blank=True)
#     item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
#     item_proposal = models.ForeignKey(ItemProposal, on_delete=models.SET_NULL, null=True, blank=True)
#     consignee = models.ForeignKey(Consignee, on_delete=models.SET_NULL, null=True, blank=True)
#     date_time_agreement = models.ForeignKey(AgreedConsigneeHandoverDateTime, on_delete=models.SET_NULL, null=True, blank=True)
#     consignee_courier_location_agreement = models.ForeignKey(ConsigneeCourierLocation, on_delete=models.SET_NULL, null=True, blank=True)
#     all_agreements_done = models.BooleanField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'courier_handover_agreement'


# class PinVerification(models.Model):
#     id = models.AutoField(primary_key=True)
#     token = models.TextField(null=True, blank=True)
#     expires_at = models.TextField(null=True, blank=True)  # Consider changing to DateTimeField
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'pin_verification'


# class ShipperHandoverPinVerification(models.Model):
#     id = models.AutoField(primary_key=True)
#     pin = models.ForeignKey(PinVerification, on_delete=models.SET_NULL, null=True, blank=True)
#     shipper_handover_agreement = models.ForeignKey(ShipperHandoverAgreement, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'shipper_handover_pin_verification'


# class CourierHandoverPinVerification(models.Model):
#     id = models.AutoField(primary_key=True)
#     pin = models.ForeignKey(PinVerification, on_delete=models.SET_NULL, null=True, blank=True)
#     courier_handover_agreement = models.ForeignKey(CourierHandoverAgreement, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'courier_handover_pin_verification'


# class CourierPickupVerification(models.Model):
#     pickup_verification_id = models.AutoField(primary_key=True)
#     picked_up_at = models.DateTimeField(null=True, blank=True)
#     payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, null=True, blank=True)
#     shipper_handover_agreement = models.ForeignKey(ShipperHandoverAgreement, on_delete=models.SET_NULL, null=True, blank=True)
#     shipper_handover_pin_verification = models.ForeignKey(ShipperHandoverPinVerification, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'courier_pickup_verification'


# class ConsigneePickupVerification(models.Model):
#     pickup_verification_id = models.AutoField(primary_key=True)
#     shipment = models.ForeignKey(Shipment, on_delete=models.SET_NULL, null=True, blank=True)
#     picked_up_at = models.DateTimeField(null=True, blank=True)
#     consignee = models.ForeignKey(Consignee, on_delete=models.SET_NULL, null=True, blank=True)
#     payout = models.ForeignKey('Payout', on_delete=models.SET_NULL, null=True, blank=True)
#     consignee_handover_agreement = models.ForeignKey(CourierHandoverAgreement, on_delete=models.SET_NULL, null=True, blank=True)
#     courier_handover_pin_verification = models.ForeignKey(CourierHandoverPinVerification, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'consignee_pickup_verification'


# class HandoverWindows(models.Model):
#     id = models.AutoField(primary_key=True)
#     item_proposal = models.ForeignKey(ItemProposal, on_delete=models.SET_NULL, null=True, blank=True)
#     pickup_window_agreement = models.ForeignKey(PickupWindowAgreement, on_delete=models.SET_NULL, null=True, blank=True)
#     delivery_window_agreement = models.ForeignKey(DelveryWindowAgreement, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'handover_windows'


# class Sso(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     google_id = models.TextField(null=True, blank=True)

#     class Meta:
#         db_table = 'sso'


# class StripeCustomer(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'stripe_customers'


# class StripeConnectedAccountsKyc(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_kyc = models.ForeignKey(UserKyc, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'stripe_connected_accounts_kyc'
#         unique_together = ('id',)


# class StripeConnectedAccount(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     stripe_account_id = models.IntegerField(null=True, blank=True)
#     kyc = models.ForeignKey(StripeConnectedAccountsKyc, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'stripe_connected_accounts'


# class TermsOfService(models.Model):
#     id = models.AutoField(primary_key=True)
#     version = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     content = models.TextField(null=True, blank=True)
#     file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)
#     is_active = models.BooleanField(null=True, blank=True)

#     class Meta:
#         db_table = 'terms_of_service'


# class TosVersion(models.Model):
#     id = models.AutoField(primary_key=True)
#     terms = models.ForeignKey(TermsOfService, on_delete=models.SET_NULL, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     terms_hash = models.TextField(null=True, blank=True, help_text='Accepted document')
#     version = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

#     class Meta:
#         db_table = 'tos_version'
#         unique_together = ('id',)


# class PrivacyPolicyVersion(models.Model):
#     id = models.AutoField(primary_key=True)
#     privacy_policy_id = models.IntegerField(null=True, blank=True)
#     version = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     terms_hash = models.TextField(null=True, blank=True, help_text='Accepted document')

#     class Meta:
#         db_table = 'privacy_policy_version'
#         unique_together = ('id',)


# class PrivacyPolicy(models.Model):
#     id = models.AutoField(primary_key=True)
#     version = models.ForeignKey(PrivacyPolicyVersion, on_delete=models.SET_NULL, null=True, blank=True)
#     file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)
#     is_active = models.BooleanField(null=True, blank=True)

#     class Meta:
#         db_table = 'privacy_policy'
#         unique_together = ('id',)


# class TosAcceptance(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     terms = models.ForeignKey(TermsOfService, on_delete=models.SET_NULL, null=True, blank=True)
#     user_agent = models.TextField(null=True, blank=True)
#     ip_address = models.CharField(max_length=45, null=True, blank=True)
#     source = models.CharField(max_length=255, null=True, blank=True)
#     tos_accepted_at = models.DateTimeField(auto_now_add=True)
#     version = models.ForeignKey(TosVersion, on_delete=models.SET_NULL, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'tos_acceptance'
#         unique_together = ('id',)
#         verbose_name = 'TOS Acceptance'
#         verbose_name_plural = 'TOS Acceptances'


# class PrivacyPolicyAcceptance(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     privacy_policy = models.ForeignKey(PrivacyPolicy, on_delete=models.SET_NULL, null=True, blank=True)
#     user_agent = models.TextField(null=True, blank=True)
#     ip_address = models.CharField(max_length=45, null=True, blank=True)
#     source = models.CharField(max_length=255, null=True, blank=True)
#     policy_accepted_at = models.DateTimeField(auto_now_add=True)
#     version = models.ForeignKey(PrivacyPolicyVersion, on_delete=models.SET_NULL, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'privacy_policy_acceptances'
#         unique_together = ('id',)
#         verbose_name = 'Privacy Policy Acceptance'
#         verbose_name_plural = 'Privacy Policy Acceptances'


# class UserWallet(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     available_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     pending_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

#     class Meta:
#         db_table = 'user_wallet'


# class Payout(models.Model):
#     payout_id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     wallet = models.ForeignKey(UserWallet, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'payouts'


# class Payment(models.Model):
#     payment_id = models.AutoField(primary_key=True)
#     payment_method = models.ForeignKey('UserPaymentMethod', on_delete=models.SET_NULL, null=True, blank=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     platform_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     witheld_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
#     currency = models.TextField(null=True, blank=True)

#     class Meta:
#         db_table = 'payments'
#         unique_together = ('payment_id', 'amount')


# class UserPaymentMethod(models.Model):
#     id = models.AutoField(primary_key=True)
#     stripe_customer = models.ForeignKey(StripeCustomer, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     billing_address = models.ForeignKey(BillingAddress, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'user_payment_methods'


# class PaymentAttempt(models.Model):
#     id = models.AutoField(primary_key=True)
#     payment_method = models.ForeignKey(UserPaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'payment_attempts'


# class IssuedCard(models.Model):
#     id = models.AutoField(primary_key=True)
#     wallet = models.ForeignKey(UserWallet, on_delete=models.SET_NULL, null=True, blank=True)
#     payment_attempts = models.ForeignKey(PaymentAttempt, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'issued_card'


# class LedgerEntry(models.Model):
#     id = models.AutoField(primary_key=True)
#     account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
#     payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)

#     class Meta:
#         db_table = 'ledger_entries'


# class PaymentIntent(models.Model):
#     id = models.AutoField(primary_key=True)

#     class Meta:
#         db_table = 'payment_intents'