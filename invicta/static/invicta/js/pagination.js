window.onload = () => {
    const lis = document.getElementsByClassName('pg');
    const lisArr = Array.from(lis)
    const url = new URL(window.location.href);
    lisArr.forEach((li) => {
        url.searchParams.set('page', li.id.split('-')[2]);
        li.href = url.toString();
    })

    const next = document.getElementById('pg-next');
    if (next) {
            next.addEventListener('click', () => {
                const url2 = new URL(window.location.href);
                url2.searchParams.set('page', parseInt(url2.searchParams.get('page')) ? `${parseInt(url2.searchParams.get('page')) + 1}` : `${2}`);
                next.href = url2.toString();
            });
    }
    const prev = document.getElementById('pg-previous');
    if (prev) {
            prev.addEventListener('click', () => {
                const url2 = new URL(window.location.href);
                url2.searchParams.set('page', parseInt(url2.searchParams.get('page')) ? `${parseInt(url2.searchParams.get('page')) - 1}` : `${2}`);
                prev.href = url2.toString();
            });    
    }
}