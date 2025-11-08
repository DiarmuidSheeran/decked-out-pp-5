# Bug Fix: Discount Code Calculation in Shopping Bag

## Bug Description

**Location:** `bag/contexts.py`, line 42

**Severity:** Critical - Affects core e-commerce functionality

**Issue:** The discount code logic had a comparison operator (`==`) instead of a conditional statement (`if`), causing the discount calculation to never execute. This meant that discount codes were stored in the session but never actually applied to the shopping bag total.

### Original Code (Buggy)
```python
if discount_code_id:
    try:
        discount_code = DiscountCode.objects.get(id=discount_code_id)
        discount_code.discount_type == 'percentage'  # ❌ Useless comparison
        discount_amount = (total * discount_code.discount_amount) / 100
        discount_amount = min(discount_amount, total)
    except DiscountCode.DoesNotExist:
        discount_amount = 0
```

### Fixed Code
```python
if discount_code_id:
    try:
        discount_code = DiscountCode.objects.get(id=discount_code_id)
        if discount_code.discount_type == 'percentage':  # ✅ Proper conditional
            discount_amount = (total * discount_code.discount_amount) / 100
            discount_amount = min(discount_amount, total)
    except DiscountCode.DoesNotExist:
        discount_amount = 0
```

## Impact

### Before Fix
- Discount codes could be entered and stored in the session
- The discount amount was always calculated as 0
- Customers were charged full price even with valid discount codes
- This would result in customer complaints and lost revenue

### After Fix
- Discount codes are properly validated and applied
- Percentage discounts are correctly calculated
- The discount amount is capped at the total (cannot be negative)
- Customers receive the correct discounted price

## Test Coverage

Comprehensive test suite added in `bag/tests.py` covering:

1. **Basic Functionality**
   - Bag contents without discount code
   - Bag contents with valid percentage discount
   - Bag contents with invalid discount code ID

2. **Edge Cases**
   - Discount applied to promotion prices
   - Multiple products with discount
   - Discount amount capped at total (cannot exceed)

3. **Integration**
   - Product promotion prices honored
   - Correct calculation with mixed regular and promotion prices

### Test Execution

To run the tests:
```bash
python manage.py test bag.tests -v 2
```

Expected output: All 8 tests should pass.

## Manual Testing Checklist

- [ ] Add product to bag
- [ ] Navigate to checkout
- [ ] Apply valid discount code
- [ ] Verify discount is reflected in bag total
- [ ] Verify discount is reflected in grand total
- [ ] Complete checkout and verify order total is correct
- [ ] Test with promotion-priced products
- [ ] Test with multiple products
- [ ] Test with invalid discount code (should show error)
- [ ] Test with expired discount code (should show error)

## Related Files Modified

1. `bag/contexts.py` - Fixed discount calculation logic
2. `bag/tests.py` - Added comprehensive test suite

## Additional Bugs Identified (Not Fixed in This PR)

During the code review, several other bugs were identified:

1. **`checkout/views.py:318`** - Reference to undefined `self` in function-based view
2. **`checkout/views.py:326`** - Double subtraction of discount amount
3. **`products/views.py:382`** - Duplicate line `sort_by = request.GET.get('sort_by')`
4. **`products/views.py:218`** - Incorrect message text ("removed" should be "added")

These should be addressed in separate bug fix PRs.

## Deployment Notes

- No database migrations required
- No environment variable changes needed
- Safe to deploy immediately
- Recommend testing in staging environment first
- Monitor customer feedback after deployment

## Rollback Plan

If issues arise after deployment:
1. Revert the commit
2. Redeploy previous version
3. Investigate any edge cases not covered in tests

The fix is minimal and isolated, so rollback risk is low.
