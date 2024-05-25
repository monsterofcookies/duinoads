document.addEventListener('DOMContentLoaded', function() {
    const adTypeElement = document.getElementById('adType');
    const bannerInputs = document.getElementById('bannerInputs');
    const impressionInputs = document.getElementById('impressionInputs');

    adTypeElement.addEventListener('change', function() {
        const selectedAdType = adTypeElement.value;

        if (selectedAdType === 'banner') {
            bannerInputs.classList.remove('hidden');
            impressionInputs.classList.add('hidden');
        } else if (selectedAdType === 'impressions') {
            impressionInputs.classList.remove('hidden');
            bannerInputs.classList.add('hidden');
        } else {
            bannerInputs.classList.add('hidden');
            impressionInputs.classList.add('hidden');
        }
    });
});
