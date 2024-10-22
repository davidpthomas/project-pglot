import express from 'express'
import { AppContext } from './config'

const createRouter = (ctx: AppContext) => {
  const router = express.Router()
  router.get('/.well-known/did.json', handleDidJsonRequest(ctx))
  return router
}

const handleDidJsonRequest = (ctx: AppContext) => (_req, res) => {
  if (!ctx.cfg.serviceDid.endsWith(ctx.cfg.hostname)) {
    return res.sendStatus(404)
  }
  res.json({
    '@context': ['https://www.w3.org/ns/did/v1'],
    id: ctx.cfg.serviceDid,
    service: [
      {
        id: '#bsky_fg',
        type: 'BskyFeedGenerator',
        serviceEndpoint: `https://${ctx.cfg.hostname}`,
      },
    ],
  })
}

export { createRouter }

export default makeRouter
