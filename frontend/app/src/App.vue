<template>
    <Nav/>

    <main>
        <router-view/>
    </main>
</template>

<script>
    import Nav from "@/components/Nav";

    export default {
        components: {Nav}
    }
</script>

<style>

    html, body, div, span, applet, object, iframe,
    h1, h2, h3, h4, h5, h6, p, blockquote, pre,
    abbr, acronym, address, big, cite, code,
    del, dfn, em, img, ins, kbd, q, s, samp,
    small, strike, strong, sub, sup, tt, var,
    b, u, i, center,
    dl, dt, dd, ol, ul, li,
    fieldset, form, label, legend,
    table, caption, tbody, tfoot, thead, tr, th, td,
    article, aside, canvas, details, embed,
    figure, figcaption, footer, header, hgroup,
    menu, nav, output, ruby, section, summary,
    time, mark, audio, video {
        margin: 0;
        padding: 0;
        border: 0;
        font-size: 100%;
        vertical-align: baseline;
    }
    a {
        color: #4B0082;
        text-decoration: none;
    }
    /* HTML5 display-role reset for older browsers */
    article, aside, details, figcaption, figure,
    footer, header, hgroup, menu, nav, section {
        display: block;
    }
    body {
        line-height: 1;
    }
    ol, ul {
        list-style: none;
    }
    blockquote, q {
        quotes: none;
    }
    blockquote:before, blockquote:after,
    q:before, q:after {
        content: none;
    }
    table {
        border-collapse: collapse;
        border-spacing: 0;
    }
    svg {
        display: flex;
        align-items: center;
    }
    .wrapper {
        padding: 0 75px;
    }
    .section_container_block {
        background-color: #FFDBCA;
    }

    .container_content_block p {
        font-family: 'Linden Hill', serif;
        font-size: 30px;
        line-height: 1.5;
    }


    /* GET STARTED */


    .form-signin {
        max-width: 330px;
        padding: 15px;
    }

    .form-signin input[type="email"] {
        margin-bottom: -1px;
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }

    .form-signin input[type="password"] {
        margin-bottom: 10px;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }
</style>
