document.addEventListener('DOMContentLoaded', () => {

    const bookname = document.getElementsByTagName("title")[0].innerText

    window.addEventListener('load', async () => {
        const state = await getScrollY(bookname)
        this.scrollTo({ top: state.scroll_y })
    });

    window.addEventListener('scrollend', async () => {

        const scrollY = this.scrollY;
        const response = await setScrollY(bookname, scrollY);

    });

});

async function getScrollY(bookName) {

    const response = await fetch(`/get-y-axis/${bookName}`);

    if (!response.ok) {
        console.error('Error on getScrollY')
    }

    const result = await response.json();
    return result;

}

async function setScrollY(ebookName, scrollY) {
    /**
     * Questa funzione deve chiamare l'api per salvare
     * la posizione scrollY del libro aperto.
     */

    const headers = new Headers({ 'Content-Type': 'application/json' })

    const body = {
        "ebookName": ebookName,
        "scrollY": scrollY
    }

    const request = new Request("/set-y-axis", {
        headers: headers,
        method: "POST",
        body: JSON.stringify(body)
    });

    const response = await fetch(request);
    if (!response.ok) {
        console.error('Error on setScrollY')
    }

    const result = await response.json();

    return 201;
}