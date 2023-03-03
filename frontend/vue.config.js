module.exports = {
    devServer: {
        proxy: 'http://localhost:8000',
        headers: {
            'Access-Control-Allow-Origin': '*',
            //'Access-Control-Allow-Credentials': true,
            'Cache-Control': null,
            'X-Requested-With': null,
            'Content-Type': 'text/html',

        },

    }
} 