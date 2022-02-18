function getArgument(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');

    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);

    if (!results) return null;
    if (!results[2]) return '';

    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

(document.onload = () => {
    let form = document.getElementById('form');
    let text, version, audio;

    form.onsubmit = (e) => {
        e.preventDefault();
        text = document.getElementById('text').value;
        version = getArgument('version');
        
        if (version === null)
            version = 'geo_m1';

        if (text === '') {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Please fill text input!'
            });

            return;
        }

        audio = new Audio(`/api/v1/speak?text=${text}&version=${version}`);

        if (audio.error === null) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Something went wrong!'
            });

            return;
        }

        audio.addEventListener('canplaythrough', () => {
            audio.play();
        });

        document.getElementById('text').value = '';
    }
})();